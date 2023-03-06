from rest_framework import serializers

class TeamSaleRequestSerializer(serializers.Serializer):
    saleIds = serializers.ListField(
        child=serializers.IntegerField(), allow_null=True
    )

