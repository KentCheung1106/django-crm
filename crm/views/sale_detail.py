from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..models.sale import Sale
from ..serializers.sale import SaleSerializer
from ..serializers.sale_request import SaleRequestSerializer
from ..services.sale import SaleService


class SaleDetailView(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
    ):
    # API endpoint that allows creation of a new crm
    queryset = Sale.objects.all()
    lookup_field = 'id'
    serializer_class = SaleRequestSerializer

    def get(self, request, sale_id=None):
        service = SaleService()
        return Response(service.getById(sale_id))

    def put(self, request, sale_id):
        service = SaleService()
        try:
            return Response(service.update(sale_id, request.data))
        except Exception as e:
            return JsonResponse({'error': True, 'content': str(e)}, status=400)
