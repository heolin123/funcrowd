import pandas as pd

from modules.aggregation.consts import SEPARATOR
from modules.aggregation.models.aggregations.base import BaseAggregation, AggregationResult
from tasks.models import Item

MIN_PROBABILITY_THRESHOLD = 0.5


def preprocess_list_column(df, column):
    column_values = df[column].apply(pd.Series).stack().reset_index(level=1, drop=True)
    df = df.drop(column, axis=1)
    df = df.join(column_values.rename(column))
    return df


def get_column_values(group, column):
    counts = group[column].value_counts()
    support = counts.iloc[0]
    answer = counts.index[0]
    probability = (support / counts.sum()).round(2)
    return answer, probability, support


def get_list_column_values(group, column):
    group = preprocess_list_column(group, column)
    counts = group[column].value_counts()
    top_counts = counts[counts/counts.sum() >= MIN_PROBABILITY_THRESHOLD]
    if not len(top_counts):
        top_counts = counts
    answer = SEPARATOR.join(map(str, top_counts.index))
    probability = SEPARATOR.join(map(str, (top_counts / counts.sum()).round(2)))
    support = SEPARATOR.join(map(str, top_counts))
    return answer, probability, support
  

class VotingAggregation(BaseAggregation):

    def _logic(self, df):
        columns = [c for c in list(df) if c not in ['user', 'item']]
        df_results = pd.DataFrame()
        for index, group in df.groupby('item'):
            item = Item.objects.get(id=index)

            for column in columns:
                column_type = item.template.fields.get(name=column).type
                if column_type == 'list':
                    answer, probability, support = get_list_column_values(group, column)
                else:
                    answer, probability, support = get_column_values(group, column)

                df_results.loc[index, column] = answer
                df_results.loc[index, column + '_prob'] = probability
                df_results.loc[index, column + '_support'] = support

        results = []
        for item_id, row in df_results.iterrows():
            data = dict(row)
            results.append(AggregationResult(item_id, data))
        return results
