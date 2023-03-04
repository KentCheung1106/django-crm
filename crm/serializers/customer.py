from rest_framework import serializers

from ..models.customer import Customer
from .simple_sale import SimpleSaleSerializer


class CustomerSerializer(serializers.ModelSerializer):
    salePerson = SimpleSaleSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Customer
        fields = '__all__'
