from django.db import models

# Create your models here.
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=240)
    code = models.CharField(max_length=240, db_index=True, unique=True)
    domain = models.CharField(max_length=240)
    department = models.CharField(max_length=240)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name