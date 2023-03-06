from django.core.exceptions import BadRequest, ObjectDoesNotExist
from django.db import transaction
from ..models.team import Team
from ..serializers.team import TeamSerializer


class TeamService:
    def create(self, dto):
        team = Team.objects.create(**dto)
        return TeamSerializer(team).data

    def getAll(self):
        teams = Team.objects.all().order_by('code')
        return list(map(lambda n: TeamSerializer(n).data, teams))

    def getByCode(self, code: str):
        try:
            team = Team.objects.get(code=code)
            return TeamSerializer(team).data
        except ObjectDoesNotExist:
            return None

    def update(self, code: str, dto: TeamSerializer):
        if 'code' in dto:
            raise BadRequest('Team code cannot be updated')
        try:
            with transaction.atomic():
                team = Team.objects.get(code=code)

                for attr, value in dto.items():
                    setattr(team, attr, value)
                team.save()

                return self.getByCode(code)
        except Exception as e:
            raise BadRequest(e)
