from rest_framework import serializers
from ..models.team import Team


class SimpleTeamSerializer(serializers.ModelSerializer):
    code = serializers.CharField(allow_blank=True, allow_null=True)
    class Meta:
        model = Team
        fields = '__all__'

