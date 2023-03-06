from rest_framework import serializers
from .simple_sale import SimpleSaleSerializer
from ..models.team import Team


class TeamSerializer(serializers.ModelSerializer):
    sales = SimpleSaleSerializer(read_only=True, many=True, allow_null=True)
    code = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Team
        fields = '__all__'

