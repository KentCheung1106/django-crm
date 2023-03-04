from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..models.sale import Sale
from ..serializers.sale import SaleSerializer
from ..services.sale import SaleService


class SaleView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    # API endpoint that allows creation of a new crm
    queryset = Sale.objects.all()
    lookup_field = 'id'
    serializer_class = SaleSerializer

    def get(self, request, sale_id=None):
        service = SaleService()
        if id:
            return Response(service.getById(sale_id))
        else:
            return Response(service.getAll())

    def post(self, request):
        service = SaleService()
        return Response(service.create(request.data))


    def put(self, request, sale_id):
        service = SaleService()
        try:
            return Response(service.update(sale_id, request.data))
        except Exception as e:
            return JsonResponse({'error': True, 'content': str(e)}, status=400)

    # def delete(self, request, id=None):
    #     return self.destroy(request, id)
