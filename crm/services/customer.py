from django.core.exceptions import BadRequest
from django.db import transaction
from ..models.customer import Customer
from ..models.sale import Sale
from ..serializers.customer import CustomerSerializer


class CustomerService:
    def create(self, dto: CustomerSerializer):
        try:
            with transaction.atomic():
                dto['salePerson'] = Sale.objects.get(id=dto['salePerson']) if 'salePerson' in dto else None
                customer = Customer.objects.create(**dto)
            return CustomerSerializer(customer).data
        except Exception as e:
            raise BadRequest(e)

    def getAll(self):
        customers = Customer.objects.all().order_by('-created', '-id')
        return list(map(lambda n: CustomerSerializer(n).data, customers))

    def getById(self, id):
        customer = Customer.objects.get(id=id)
        return CustomerSerializer(customer).data

    def update(self, id: int, dto: CustomerSerializer):
        try:
            with transaction.atomic():
                customer = Customer.objects.select_for_update().get(id=id)
                for attr, value in dto.items():
                    if attr == 'salePerson':
                        setattr(customer, attr, Sale.objects.get(id=value))
                    else:
                        setattr(customer, attr, value)

                customer.save()

                return self.getById(id)
        except Exception as e:
            raise BadRequest(e)
