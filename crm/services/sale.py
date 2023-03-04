from django.core.exceptions import BadRequest
from django.db import transaction

from ..models.sale import Sale
from ..serializers.sale import SaleSerializer


class SaleService:
    def create(self, dto):
        sale = Sale.objects.create(**dto)
        return SaleSerializer(sale).data

    def getAll(self):
        sales = Sale.objects.all().order_by('-created', '-id')
        return list(map(lambda n: SaleSerializer(n).data, sales))

    def getById(self, id):
        sale = Sale.objects.get(id=id)
        return SaleSerializer(sale).data

    def update(self, id: int, dto: SaleSerializer):
        try:
            with transaction.atomic():
                sale = Sale.objects.get(id=id)

                for attr, value in dto.items():
                    setattr(sale, attr, value)
                sale.save()

                return self.getById(id)
        except Exception as e:
            raise BadRequest(e)
