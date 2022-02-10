# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Substances(models.Model):
    """Substances model"""
    id = models.AutoField(primary_key=True)
    subid = models.CharField(max_length=512)
    casno = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=3)
    formula = models.CharField(max_length=1024, blank=True, null=True)
    formula_html = models.CharField(max_length=1024, blank=True, null=True)
    pcformula = models.CharField(max_length=256)
    molweight = models.FloatField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'substances'


class Chemicals(models.Model):
    """Chemicals model"""
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    substances = models.ForeignKey(Substances, models.DO_NOTHING, db_column="substance_id")
    subid = models.CharField(max_length=50)
    sys_id = models.CharField(max_length=50, blank=True, null=True)
    report_id = models.IntegerField()
    compnum = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    comments = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255)
    compnumcheck = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chemicals'


class Identifiers(models.Model):
    """ Identifiers table model """
    id = models.AutoField(primary_key=True)
    # substance_id = models.IntegerField()
    substances = models.ForeignKey(Substances, models.DO_NOTHING, db_column="substance_id")
    type = models.CharField(max_length=12)
    value = models.CharField(max_length=1024)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identifiers'


class Systems(models.Model):
    """ Systems table model """
    id = models.AutoField(primary_key=True)
    sysnmid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512)
    volume = models.IntegerField()
    publication_id = models.SmallIntegerField()
    components = models.PositiveIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'systems'


class SubstancesSystems(models.Model):
    """ Substances_systems table model """
    id = models.AutoField(primary_key=True)
    substances = models.ForeignKey(Substances, models.DO_NOTHING, db_column="substance_id")
    systems = models.ForeignKey(Systems, models.DO_NOTHING, db_column="system_id")
    # substance_id = models.IntegerField(blank=True, null=True)
    # system_id = models.IntegerField(blank=True, null=True)
    sysid = models.CharField(max_length=10, blank=True, null=True)
    subid = models.CharField(max_length=10, blank=True, null=True)
    sysnmid = models.CharField(max_length=10, blank=True, null=True)
    component_index = models.IntegerField(blank=True, null=True)
    issolvent = models.IntegerField(db_column='isSolvent', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'substances_systems'
