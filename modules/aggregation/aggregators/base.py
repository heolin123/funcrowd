from typing import List

import pandas as pd
from django.apps import apps
from django.db import transaction

from modules.aggregation.aggregators.field_result import FieldResult
from modules.aggregation.aggregators.item_result import ItemResult
from modules.aggregation.aggregators.utils import decompose_list_column
from modules.aggregation.consts import EMPTY_VALUE

MIN_PROBABILITY_THRESHOLD = 0.5


class BaseAggregator:
    """
    Aggregates annotations and selects final answer for each
    annotation field in the item.

    Aggregation can be performed for all items in the task at once,
    or, if item object is passed in the constructor, just a single item.
    """

    def __init__(self, task, item=None, exclude_skipped=False):
        self.task = task
        self.item = item

        if self.item:
            self.template = self.item.template
        else:
            # if aggregation is done for the whole task, it will assume
            # that all items share the same template
            self.template = self.task.items.first().template

        self.exclude_skipped = exclude_skipped

    def _get_annotations_table(self) -> pd.DataFrame:
        """
        Generates a data frame with all values for annotations
        from all fields from all users.

        :return: pd.DataFrame,
        """
        Annotation = apps.get_model("tasks.Annotation")
        result = []

        annotations = Annotation.objects.filter(item__task=self.task).exclude(user=None)
        if self.item:
            annotations = annotations.filter(item_id=self.item)
        if self.exclude_skipped:
            annotations = annotations.exclude(skipped=True)

        for data, item, user in annotations.values_list("data", "item", "user__username"):
            data['item'] = item
            data['user'] = user
            for field in self.template.annotations_fields:
                if field.name not in data:
                    data[field.name] = None
            result.append(data)
        return pd.DataFrame(result).fillna(EMPTY_VALUE)

    def _get_field_result(self, group: pd.DataFrame, field_name: str) -> FieldResult:
        """
        Aggregates answers for selected field for one item, selects most frequent
        answer as the final one. Probability is computed as percentage frequency.

        :param group: pd.DataFrame, contains all answers for one item
        :param field_name: field for which we want to find the result answer
        :return: ValueFieldResult
        """
        # making sure the index is sorted for values with the same count
        counts = group[field_name].value_counts().sort_index(
            ascending=False).sort_values(ascending=False)

        answer = str(counts.index[0])
        support = int(counts.iloc[0])
        probability = float((support / counts.sum()).round(2))
        return FieldResult(answer, probability, support)

    def _get_list_field_result(self, group: pd.DataFrame, field_name: str) -> List[FieldResult]:
        """
        Aggregates answer for selected field containing a list of values.
        Selects a list of most frequent values as a results.
        In this implementation all answers with probability value are
        over MIN_PROBABILITY_THRESHOLD are accepted in the final list.

        :param group: pd.DataFrame, contains all answers for one item
        :param field_name: field for which we want to find the result answer
        :return: ListFieldResult
        """

        df_group = decompose_list_column(group, field_name)
        df_counts = df_group[field_name].value_counts().to_frame(name="counts")
        df_counts['probability'] = df_counts['counts'] / len(group)

        # select only answers, which probability is over the threshold
        df_results = df_counts[df_counts['probability'] >= MIN_PROBABILITY_THRESHOLD]
        if not len(df_results):
            df_results = df_counts
        df_results = df_results.sort_index()

        answers = list(df_results.index)
        probabilities = list(df_results['probability'].round(2))
        supports = list(df_results['counts'])

        return [
            FieldResult(answer, probability, support)
            for (answer, probability, support) in
            zip(answers, probabilities, supports)
        ]

    def _get_fields_types(self):
        Item = apps.get_model("tasks.Item")

        fields_types = {}
        if self.task:
            _items = Item.objects.filter(task=self.task)
        else:
            _items = Item.objects.filter(task=self.item.task)
        for value in _items.values(
                'template__fields__name', 'template__fields__type').distinct():
            fields_types[value['template__fields__name']] = value['template__fields__type']
        return fields_types

    def _logic(self, df: pd.DataFrame) -> List[ItemResult]:
        """
        Aggregates annotations done for items and selects, one final answer

        :param df: annotation table, result from `_get_annotations_table`
        :return: a list of ItemResult, one for each item
        """
        fields_names = [c for c in list(df) if c not in ['user', 'item']]
        fields_types = self._get_fields_types()

        item_results = []

        if not len(df):
            return item_results

        for item_id, group in df.groupby('item'):
            item_result = ItemResult(item_id, len(group))

            for field_name in fields_names:
                column_type = fields_types[field_name]
                if column_type == 'list':
                    field_results = self._get_list_field_result(group, field_name)
                    for field_result in field_results:
                        item_result.add_answer(field_name, field_result)
                else:
                    field_result = self._get_field_result(group, field_name)
                    item_result.add_answer(field_name, field_result)

            item_results.append(item_result)
        return item_results

    @transaction.atomic
    def aggregate(self):
        """
        Performs aggregation of answers for selected item/items,
        and updates ItemAggregation objects with the new values.

        :return: List[ItemAggregation]
        """
        ItemAggregation = apps.get_model("aggregation.ItemAggregation")
        aggregations = []
        for result in self._logic(self._get_annotations_table()):
            aggregation, _ = ItemAggregation.objects.get_or_create(item_id=result.item_id)
            aggregation.data = result.to_json()
            aggregation.type = self.__class__.__name__
            aggregation.save()
            aggregations.append(aggregation)
        return aggregations
