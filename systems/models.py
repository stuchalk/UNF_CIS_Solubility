from django.db import models


class Systems(models.Model):
    sysnmid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512, db_collation='utf8_general_ci')
    volume = models.IntegerField()
    publication_id = models.SmallIntegerField()
    components = models.PositiveIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'systems'
