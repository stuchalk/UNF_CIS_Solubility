""" django models file for reports app """
from django.db import models


class Authors(models.Model):
    """ authors table model """
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    abbrev = models.CharField(max_length=128, blank=True, null=True)
    institution = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authors'

class AuthorsReports(models.Model):
    """ authors table model """
    id = models.SmallAutoField(primary_key=True)
    author = models.ForeignKey(Authors, models.DO_NOTHING, db_column="author_id")
    rep = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    name = models.CharField(max_length=255)
    sysid = models.CharField(max_length=20)
    role = models.CharField(max_length=9)
    order = models.PositiveIntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authors_reports'


class Chemicals(models.Model):
    """ chemicals table model """
    description = models.TextField(blank=True, null=True)
    sub = models.ForeignKey("Substances", models.DO_NOTHING, db_column="substance_id")
    subid = models.CharField(max_length=50)
    sys_id = models.CharField(max_length=50, blank=True, null=True)
    rep = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    compnum = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    comments = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255)
    compnumcheck = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chemicals'


class Conditions(models.Model):
    """ conditions table model """
    datapoint = models.ForeignKey("Datapoints", models.DO_NOTHING, db_column="datapoint_id")
    sysid_tablenum_rownum = models.CharField(max_length=32, blank=True, null=True)
    dataseries = models.ForeignKey("Dataseries", models.DO_NOTHING, db_column="dataseries_id")
    sysid_tablenum = models.CharField(max_length=15, blank=True, null=True)
    property = models.ForeignKey("Properties", models.DO_NOTHING, db_column="property_id")
    unit = models.ForeignKey("Units", models.DO_NOTHING, db_column="unit_id")
    significand = models.CharField(max_length=16)
    exponent = models.IntegerField()
    error = models.CharField(max_length=16, blank=True, null=True)
    error_type = models.CharField(max_length=8, blank=True, null=True)
    accuracy = models.IntegerField()
    component = models.CharField(max_length=50, blank=True, null=True)
    heading = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    exact = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conditions'


class Data(models.Model):
    """ data table model """
    datapoint = models.ForeignKey("Datapoints", models.DO_NOTHING, db_column="datapoint_id")
    property = models.ForeignKey("Properties", models.DO_NOTHING, db_column="property_id")
    unit = models.ForeignKey("Units", models.DO_NOTHING, db_column="unit_id")
    sysid_tablenum_rownum = models.CharField(max_length=32)
    str_property = models.CharField(max_length=512)
    dataset = models.ForeignKey("Datasets", models.DO_NOTHING, db_column="dataset_id")
    dataseries = models.ForeignKey("Dataseries", models.DO_NOTHING, db_column="dataseries_id")
    sysid_tablenum = models.CharField(max_length=15)
    dataformat = models.CharField(max_length=5)
    significand = models.TextField()
    exponent = models.TextField()
    error = models.TextField()
    error_type = models.CharField(max_length=8)
    unit_string = models.CharField(max_length=16, blank=True, null=True)
    accuracy = models.TextField()
    exact = models.IntegerField()
    component = models.CharField(max_length=50, blank=True, null=True)
    heading = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data'


class Datapoints(models.Model):
    """ datapoints table model """
    dataset = models.ForeignKey("Datasets", models.DO_NOTHING, db_column="dataset_id")
    dataseries = models.ForeignKey("Dataseries", models.DO_NOTHING, db_column="dataseries_id")
    sysid = models.CharField(max_length=15, blank=True, null=True)
    tablenum = models.SmallIntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=10, blank=True, null=True)
    sysid_tablenum_rownum = models.CharField(max_length=32, blank=True, null=True)
    rownum = models.SmallIntegerField(blank=True, null=True)
    row_index = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'datapoints'


class Dataseries(models.Model):
    """ dataseries table model """
    id = models.SmallAutoField(primary_key=True)
    dataset = models.ForeignKey("Datasets", models.DO_NOTHING, db_column="dataset_id")
    sysid = models.CharField(max_length=15, blank=True, null=True)
    tablenum = models.SmallIntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20)
    heading = models.CharField(max_length=512)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dataseries'


class Datasets(models.Model):
    """ datasets table model """
    sysid = models.CharField(max_length=10)
    sysnmid = models.PositiveIntegerField()
    report = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    reference = models.ForeignKey("References", models.DO_NOTHING, db_column="reference_id")
    system = models.ForeignKey("Systems", models.DO_NOTHING, db_column="system_id")
    comments = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'datasets'


class Identifiers(models.Model):
    """ indentifiers table model """

    sub = models.ForeignKey("Substances", models.DO_NOTHING, db_column="substance_id")
    type = models.CharField(max_length=12)
    value = models.CharField(max_length=1024)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identifiers'


class Properties(models.Model):
    """ properties table model """
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=32)
    definition = models.CharField(max_length=512)
    source = models.CharField(max_length=256)
    baseunit = models.ForeignKey("Units", models.DO_NOTHING, db_column="unit_id")
    quantity_id = models.SmallIntegerField(blank=True, null=True)
    field = models.CharField(max_length=256)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'properties'


class Publications(models.Model):
    """ publications table model """
    id = models.SmallAutoField(primary_key=True)
    volumeid = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=128)
    series = models.CharField(max_length=64)
    volume = models.CharField(max_length=32, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=512)
    url = models.CharField(max_length=128)
    citation = models.CharField(max_length=128, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'publications'


class References(models.Model):
    """ references model """
    refid = models.IntegerField(blank=True, null=True)
    report = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    method = models.TextField(blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    sysid = models.CharField(max_length=50, blank=True, null=True)
    journal = models.CharField(max_length=128, blank=True, null=True)
    publisher = models.CharField(max_length=256, blank=True, null=True)
    abbrev = models.CharField(max_length=128, blank=True, null=True)
    authors = models.CharField(max_length=2048, blank=True, null=True)
    authorslong = models.CharField(max_length=1024, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    volume = models.CharField(max_length=6, blank=True, null=True)
    issue = models.CharField(max_length=16, blank=True, null=True)
    startpage = models.CharField(max_length=6, blank=True, null=True)
    endpage = models.CharField(max_length=6, blank=True, null=True)
    title = models.CharField(max_length=1024, blank=True, null=True)
    citelong = models.CharField(max_length=1024, blank=True, null=True)
    citeshort = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    doi = models.CharField(max_length=256, blank=True, null=True)
    rcount = models.PositiveIntegerField(blank=True, null=True)
    ecount = models.PositiveIntegerField(blank=True, null=True)
    crossref = models.CharField(max_length=3)
    refnum = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=13)
    duplicate = models.PositiveSmallIntegerField(blank=True, null=True)
    unique = models.CharField(max_length=3)
    comments = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'references'


class Reports(models.Model):
    """ reports table model """
    pub = models.ForeignKey(Publications, models.DO_NOTHING, db_column="publication_id")
    sysid = models.CharField(max_length=10)
    eval = models.IntegerField(blank=True, null=True)
    count = models.SmallIntegerField()
    variables = models.CharField(max_length=512, blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=256)
    page = models.CharField(max_length=8)
    comment = models.CharField(max_length=2048)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reports'


class Substances(models.Model):
    """ substances table model """
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


class SubstancesSystems(models.Model):
    """ substances_systems table model """
    substance = models.ForeignKey(Substances, models.DO_NOTHING, db_column="substance_id")
    system = models.ForeignKey("Systems", models.DO_NOTHING, db_column="system_id")
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


class Systems(models.Model):
    """ systems table model """
    sysnmid = models.ForeignKey("Datasets", models.DO_NOTHING, db_column="sysnmid")
    # sysnmid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512)
    volume = models.IntegerField()
    publication_id = models.SmallIntegerField()
    components = models.PositiveIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'systems'


class Units(models.Model):
    """ unit table model """
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    quantity_id = models.SmallIntegerField(blank=True, null=True)
    symbol = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=9, blank=True, null=True)
    unitsml_id = models.CharField(max_length=10, blank=True, null=True)
    exact = models.IntegerField()
    factor = models.FloatField()
    si_equivalent = models.CharField(max_length=32, blank=True, null=True)
    unitstring = models.CharField(max_length=32, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'units'
