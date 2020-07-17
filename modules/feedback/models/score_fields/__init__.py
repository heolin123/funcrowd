from .base import FeedbackScore
from .reference_score import ReferenceScore
from .voting_score import VotingScore
from .regression_reference_score import RegressionReferenceScore


SCORE_FIELDS = {}
for cls in FeedbackScore.__subclasses__():
    SCORE_FIELDS[cls.__name__] = cls
