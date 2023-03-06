from django.core.exceptions import BadRequest
from django.db import transaction

from ..models.customer import Customer
from ..models.sale import Sale
from ..models.team import Team
from ..serializers.customer import CustomerSerializer
from ..serializers.sale_customer_request import SaleCustomerRequestSerializer
from ..serializers.simple_sale import SimpleSaleSerializer
from ..serializers.team_sale_request import TeamSaleRequestSerializer


class TeamSaleService:
    def getTeamSales(self, code: str):
        team_sales = Sale.objects.filter(team__code=code).prefetch_related('team').all()
        return SimpleSaleSerializer(team_sales, many=True).data

    def update(self, code: str, dto: TeamSaleRequestSerializer):
        try:
            with transaction.atomic():
                team = Team.objects.select_for_update().get(code=code)
                sales = Sale.objects.filter(id__in=dto['saleIds'])
                team.sales.add(*sales)

                team.save()

                return SimpleSaleSerializer(team.sales.all(), many=True).data
        except Exception as e:
            raise BadRequest(e)
