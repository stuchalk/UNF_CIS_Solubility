""" crosswalks models """
from sds.models import *


class Contexts(models.Model):
    """ model for the contexts table """
    dataset = models.ForeignKey("sds.Datasets", models.DO_NOTHING, db_column="dataset_id")
    # dataset_id = models.IntegerField()
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contexts'


class Nspaces(models.Model):
    """ model for the nspaces table """
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    ns = models.CharField(max_length=8)
    path = models.CharField(unique=True, max_length=128)
    homepage = models.CharField(max_length=128)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nspaces'


class Ontterms(models.Model):
    """ model for the onterms table """
    id = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=256)
    definition = models.CharField(max_length=2048, blank=True, null=True)
    code = models.CharField(max_length=64)
    url = models.CharField(max_length=512, blank=True, null=True)
    nspace = models.ForeignKey("Nspaces", models.DO_NOTHING, db_column="nspace_id")
    # nspace_id = models.SmallIntegerField()
    sdsection = models.CharField(max_length=11, blank=True, null=True)
    sdsubsection = models.CharField(max_length=64, blank=True, null=True)
    to_remove = models.CharField(max_length=8, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ontterms'


class Crosswalks(models.Model):
    """ model for the crosswalks table """
    context = models.ForeignKey("Contexts", models.DO_NOTHING, db_column="context_id")
    # dataset = models.ForeignKey("Datasets", models.DO_NOTHING, db_column="dataset_id")
    table = models.CharField(max_length=128, blank=True, null=True)
    field = models.CharField(max_length=256, blank=True, null=True)
    filter = models.CharField(max_length=128, blank=True, null=True)
    cardinality = models.PositiveIntegerField(blank=True, null=True)
    ontterm_id = models.IntegerField(blank=True, null=True)
    sdsection = models.CharField(max_length=11, blank=True, null=True)
    sdsubsection = models.CharField(max_length=128, blank=True, null=True)
    sdsubsubsection = models.CharField(max_length=64, blank=True, null=True)
    newname = models.CharField(max_length=32, blank=True, null=True)
    category = models.CharField(max_length=64, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)
    datatype = models.CharField(max_length=8, blank=True, null=True)
    intlinks = models.CharField(max_length=1024, blank=True, null=True)
    meta = models.CharField(max_length=64, blank=True, null=True)
    ignore = models.CharField(max_length=32, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'crosswalks'
