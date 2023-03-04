from django.db import models

# Create your models here.
from django.db import models


class Sale(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField(null=True)
    company = models.CharField(max_length=240)
    department = models.CharField(max_length=240)
    team = models.CharField(max_length=240)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sale'

    def __str__(self):
        return self.name