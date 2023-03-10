from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..models.customer import Customer
from ..serializers.customer import CustomerSerializer
from ..serializers.customer_request import CustomerRequestSerializer
from ..services.customer import CustomerService


class CustomerView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
    ):
    # API endpoint that allows creation of a new crm
    queryset = Customer.objects.all()
    lookup_field = 'id'
    serializer_class = CustomerRequestSerializer

    def get(self, request):
        service = CustomerService()
        return Response(service.getAll())

    def post(self, request):
        service = CustomerService()
        return Response(service.create(request.data))
