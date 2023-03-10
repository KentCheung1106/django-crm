from rest_framework import serializers
from .customer import CustomerSerializer
from .simple_team import SimpleTeamSerializer
from ..models.sale import Sale


class SaleSerializer(serializers.ModelSerializer):
    customers = CustomerSerializer(read_only=True, many=True, allow_null=True)
    team = SimpleTeamSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Sale
        fields = '__all__'

