from django.db import models
from .models import *


class Datasets(models.Model):
    sysid = models.CharField(max_length=10)
    sysnmid = models.PositiveIntegerField()
    report_id = models.IntegerField()
    system_id = models.IntegerField()
    reference_id = models.IntegerField()
    comments = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
