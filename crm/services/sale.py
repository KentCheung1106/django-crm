from django.core.exceptions import BadRequest
from django.db import transaction

from ..models.sale import Sale
from ..models.team import Team
from ..serializers.sale import SaleSerializer
from ..serializers.sale_request import SaleRequestSerializer


class SaleService:
    def create(self, dto: SaleRequestSerializer):
        try:
            with transaction.atomic():
                dto['team'] = Team.objects.get(id=dto['team']) if 'team' in dto else None
                sale = Sale.objects.create(**dto)
            return SaleSerializer(sale).data
        except Exception as e:
            raise BadRequest(e)

    def getAll(self):
        sales = Sale.objects.all().order_by('-created', '-id')
        return list(map(lambda n: SaleSerializer(n).data, sales))

    def getById(self, id):
        sale = Sale.objects.get(id=id)
        return SaleSerializer(sale).data

    def update(self, id: int, dto: SaleRequestSerializer):
        try:
            with transaction.atomic():
                sale = Sale.objects.get(id=id)

                for attr, value in dto.items():
                    if attr == 'team':
                        setattr(sale, attr, Team.objects.get(id=value))
                    else:
                        setattr(sale, attr, value)

                sale.save()

                return self.getById(id)
        except Exception as e:
            raise BadRequest(e)
