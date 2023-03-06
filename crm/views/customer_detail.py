from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..models.customer import Customer
from ..serializers.customer_request import CustomerRequestSerializer
from ..services.customer import CustomerService


class CustomerDetailView(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin):
    # API endpoint that allows creation of a new crm
    queryset = Customer.objects.all()
    lookup_field = 'id'
    serializer_class = CustomerRequestSerializer

    def get(self, request, id):
        service = CustomerService()
        return Response(service.getById(id))


    def put(self, request, id):
        service = CustomerService()
        try:
            return Response(service.update(id, request.data))
        except Exception as e:
            return JsonResponse({'error': True, 'content': str(e)}, status=400)
