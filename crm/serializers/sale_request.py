from rest_framework import serializers
from .customer import CustomerSerializer
from .simple_team import SimpleTeamSerializer
from ..models.sale import Sale


class SaleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

