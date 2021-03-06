from rest_framework import serializers
from modules.statistics.models import UserStats


class UserStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStats
        fields = ('user_id', 'annotated_documents', 'high_agreement_count', 'high_agreement_percentage',
                  'agreement_ranking_position', 'agreement_ranking_percentage',
                  'annotated_missions', 'annotated_tasks')

