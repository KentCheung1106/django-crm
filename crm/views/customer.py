from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..models.customer import Customer
from ..serializers.customer import CustomerSerializer
from ..services.customer import CustomerService


class CustomerView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    # API endpoint that allows creation of a new crm
    queryset = Customer.objects.all()
    lookup_field = 'id'
    serializer_class = CustomerSerializer

    def get(self, request, id=None):
        service = CustomerService()
        if id:
            return Response(service.getById(id))
        else:
            return Response(service.getAll())

    def post(self, request):
        service = CustomerService()
        return Response(service.create(request.data))


    def put(self, request, id):
        service = CustomerService()
        try:
            return Response(service.update(id, request.data))
        except Exception as e:
            return JsonResponse({'error': True, 'content': str(e)}, status=400)

    # def perform_update(self, serializer):
    #     serializer.save(created_by=self.request)

    def delete(self, request, id=None):
        return self.destroy(request, id)

