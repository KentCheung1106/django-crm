from rest_framework import serializers

class SaleCustomerRequestSerializer(serializers.Serializer):
    customerIds = serializers.ListField(
        child=serializers.IntegerField(), allow_null=True
    )

