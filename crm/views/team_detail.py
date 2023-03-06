from django.http import JsonResponse
from rest_framework.response import Response


from rest_framework import generics, mixins
from ..models.team import Team
from ..serializers.team import TeamSerializer
from ..services.team import TeamService


class TeamDetailView(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
    ):
    # API endpoint that allows creation of a new crm
    queryset = Team.objects.all()
    lookup_field = 'id'
    serializer_class = TeamSerializer

    def get(self, request, code: str):
        service = TeamService()
        return Response(service.getByCode(code))

    def put(self, request, code: str):
        service = TeamService()
        try:
            return Response(service.update(code, request.data))
        except Exception as e:
            return JsonResponse({'error': True, 'content': str(e)}, status=400)
