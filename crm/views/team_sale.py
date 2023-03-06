from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, mixins
from ..serializers.team_sale_request import TeamSaleRequestSerializer
from ..services.team_sale import TeamSaleService


class TeamSaleView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin):
    serializer_class = TeamSaleRequestSerializer

    def get(self, request, code):
        service = TeamSaleService()
        return Response(service.getTeamSales(code))

    def put(self, request, code):
        service = TeamSaleService()
        dto = TeamSaleRequestSerializer(request.data)

        try:
            return Response(service.update(code, dto.data))
        except Exception as e:
            return JsonResponse({'error': True, 'content': str(e)}, status=400)
