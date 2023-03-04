from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..serializers.sale_customer import SaleCustomerRequestSerializer
from ..services.sale_customer import SaleCustomerService


class SaleCustomerView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin):


    def get(self, request, sale_id):
        service = SaleCustomerService()
        return Response(service.getSaleCustomers(sale_id))

    def put(self, request, sale_id):
        service = SaleCustomerService()
        dto = SaleCustomerRequestSerializer(request.data)

        try:
            return Response(service.update(sale_id, dto.data))
        except Exception as e:
            return JsonResponse({'error': True, 'content': str(e)}, status=400)
