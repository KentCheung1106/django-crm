from django.db import models

# Create your models here.
from django.db import models

from crm.models.team import Team


class Sale(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField(null=True)
    company = models.CharField(max_length=240)
    team = models.ForeignKey(Team, related_name='sales', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sales'

    def __str__(self):
        return self.name