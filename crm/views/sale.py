from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..models.sale import Sale
from ..serializers.sale import SaleSerializer
from ..serializers.sale_request import SaleRequestSerializer
from ..services.sale import SaleService


class SaleView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
    ):
    # API endpoint that allows creation of a new crm
    queryset = Sale.objects.all()
    lookup_field = 'id'
    serializer_class = SaleRequestSerializer

    def get(self, request):
        service = SaleService()
        return Response(service.getAll())

    def post(self, request):
        service = SaleService()
        return Response(service.create(request.data))

