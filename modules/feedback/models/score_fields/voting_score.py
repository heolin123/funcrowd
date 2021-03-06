from .base import FeedbackScore
from modules.feedback.models.utils.voting import get_votings, filter_values
from tasks.field_types import LIST
import numpy as np


class VotingScore(FeedbackScore):

    def score(self, annotation):
        item = annotation.item
        field = item.template.fields.get(name=self.field)
        other_annotations = item.annotations.exclude(user=None)  # .exclude(user=annotation.user)
        if other_annotations:
            df_probs = get_votings(other_annotations, field)
            if field.type == LIST:
                scores = []
                for value in annotation.data[self.field]:
                    scores.append(df_probs.get(value, 0.0))
                score = np.average(scores)
            else:
                value = annotation.data[self.field]
                if field.data_source:
                    values = item.data[field.data_source.name]
                    value = filter_values(value, values)
                score = df_probs.get(value, 0.0)
            return score
        return None
