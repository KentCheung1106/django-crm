from rest_framework import serializers
from ..models.sale import Sale


class SimpleSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

