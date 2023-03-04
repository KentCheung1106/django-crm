# Create your models here.
from django.db import models

from .sale import Sale


# from settings.sales.models import Sale


class Customer(models.Model):
    name = models.CharField("Name", max_length=240)
    username = models.CharField("Name", max_length=240, null=True)
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    salePerson = models.ForeignKey(Sale, related_name='customers', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name
