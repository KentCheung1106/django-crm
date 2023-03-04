from django.core.exceptions import BadRequest
from django.db import transaction

from ..models.customer import Customer
from ..models.sale import Sale
from ..serializers.customer import CustomerSerializer
from ..serializers.sale_customer import SaleCustomerRequestSerializer


class SaleCustomerService:
    def getSaleCustomers(self, sale_id: int):
        sale_customers = Customer.objects.filter(salePerson=sale_id).prefetch_related('salePerson').all()
        return CustomerSerializer(sale_customers, many=True).data

    def update(self, sale_id: int, dto: SaleCustomerRequestSerializer):
        try:
            with transaction.atomic():
                sale = Sale.objects.select_for_update().get(id=sale_id)
                customers = Customer.objects.filter(id__in=dto['customerIds'])
                sale.customer_set.add(*customers)

                sale.save()

                return CustomerSerializer(sale.customer_set.all(), many=True).data
        except Exception as e:
            raise BadRequest(e)
