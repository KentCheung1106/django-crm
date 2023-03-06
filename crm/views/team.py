from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins

from ..models.sale import Sale
from ..models.team import Team
from ..serializers.sale import SaleSerializer
from ..serializers.team import TeamSerializer
from ..services.sale import SaleService
from ..services.team import TeamService


class TeamView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
    ):
    # API endpoint that allows creation of a new crm
    queryset = Team.objects.all()
    lookup_field = 'id'
    serializer_class = TeamSerializer

    def get(self, request):
        service = TeamService()
        return Response(service.getAll())

    def post(self, request):
        service = TeamService()
        return Response(service.create(request.data))

