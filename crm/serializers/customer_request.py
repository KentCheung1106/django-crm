from rest_framework import serializers

from ..models.customer import Customer


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
