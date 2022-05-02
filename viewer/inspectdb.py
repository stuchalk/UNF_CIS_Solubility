# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Authors(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    abbrev = models.CharField(max_length=128, blank=True, null=True)
    institution = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    orcid = models.CharField(max_length=20, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authors'


class AuthorsReports(models.Model):
    id = models.SmallAutoField(primary_key=True)
    author_id = models.SmallIntegerField()
    report_id = models.IntegerField()
    role = models.CharField(max_length=9)
    order = models.PositiveIntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authors_reports'


class Chemicals(models.Model):
    substance_id = models.IntegerField()
    report_id = models.IntegerField()
    supplier = models.CharField(max_length=128, blank=True, null=True)
    purity = models.CharField(max_length=128, blank=True, null=True)
    compnum = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chemicals'


class Conditions(models.Model):
    datapoints = models.ForeignKey('Datapoints', models.DO_NOTHING, db_column='datapoint_id', blank=True, null=True)
    # datapoint_id = models.IntegerField(blank=True, null=True)
    dataseries_id = models.SmallIntegerField(blank=True, null=True)
    quantities = models.ForeignKey('Quantities', models.DO_NOTHING, db_column='quantity_id', blank=True, null=True)
    # quantity_id = models.SmallIntegerField()
    text = models.CharField(max_length=16)
    significand = models.CharField(max_length=16)
    exponent = models.IntegerField()
    error = models.CharField(max_length=16, blank=True, null=True)
    error_type = models.CharField(max_length=8, blank=True, null=True)
    unit_id = models.SmallIntegerField()
    accuracy = models.PositiveIntegerField()
    compnum = models.PositiveIntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conditions'


class Data(models.Model):
    datapoints = models.ForeignKey('Datapoints', models.DO_NOTHING, db_column='datapoint_id', blank=True, null=True)
    # datapoint_id = models.IntegerField(blank=True, null=True)
    quantities = models.ForeignKey('Quantities', models.DO_NOTHING, db_column='quantity_id', blank=True, null=True)
    # quantity_id = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=16)
    significand = models.CharField(max_length=16)
    exponent = models.IntegerField()
    error = models.CharField(max_length=16, blank=True, null=True)
    error_type = models.CharField(max_length=8, blank=True, null=True)
    units = models.ForeignKey('Units', models.DO_NOTHING, db_column='unit_id', blank=True, null=True)
    # unit_id = models.SmallIntegerField()
    accuracy = models.PositiveIntegerField()
    compnum = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data'


class Datapoints(models.Model):
    title = models.CharField(max_length=128)
    datasets = models.ForeignKey('Datasets', models.DO_NOTHING, db_column='dataset_id', blank=True, null=True)
    dataseries = models.ForeignKey('Dataseries', models.DO_NOTHING, db_column='dataseries_id', blank=True, null=True)
    # dataseries_id = models.IntegerField(blank=True, null=True)
    rownum = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'datapoints'


class Dataseries(models.Model):
    id = models.SmallAutoField(primary_key=True)
    heading = models.CharField(max_length=128)
    dataset_id = models.IntegerField()
    seriesnum = models.PositiveIntegerField()
    type = models.CharField(max_length=15)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dataseries'


class Datasets(models.Model):
    title = models.CharField(db_column='title', max_length=128)
    description = models.CharField(max_length=256)
    reports = models.ForeignKey('Reports', models.DO_NOTHING, db_column='report_id', blank=True, null=True)
    # report_id = models.IntegerField()
    comments = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'datasets'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user_id', blank=True, null=True)
    # user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Evaluations(models.Model):
    id = models.SmallAutoField(primary_key=True)
    evalid = models.CharField(max_length=10, db_collation='utf8_general_ci', blank=True, null=True)
    report_id = models.IntegerField()
    title = models.CharField(max_length=256)
    raw = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    sysid = models.CharField(max_length=10, db_collation='utf8_general_ci', blank=True, null=True)
    data = models.IntegerField()
    date = models.CharField(max_length=64, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'evaluations'


class EvaluationsReferences(models.Model):
    evaluation_id = models.SmallIntegerField(blank=True, null=True)
    evalid = models.CharField(max_length=50, blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    refid = models.CharField(max_length=50, blank=True, null=True)
    citenum = models.CharField(max_length=8, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'evaluations_references'


class Identifiers(models.Model):
    substance_id = models.IntegerField()
    type = models.CharField(max_length=12)
    value = models.CharField(max_length=1024)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identifiers'


class Journals(models.Model):
    name = models.CharField(max_length=256)
    abbrev = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    homepage = models.CharField(max_length=256)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'journals'


class Properties(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=256, db_collation='utf8_general_ci')
    symbol = models.CharField(max_length=64, db_collation='utf8_general_ci')
    datafield = models.CharField(max_length=255, blank=True, null=True)
    definition = models.CharField(max_length=512, db_collation='utf8_general_ci')
    source = models.CharField(max_length=256, db_collation='utf8_general_ci')
    quantity_id = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'properties'


class Quantities(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    symbol = models.CharField(max_length=8)
    description = models.CharField(max_length=512)
    baseunit_id = models.SmallIntegerField(blank=True, null=True)
    comment = models.CharField(max_length=512)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quantities'


class References(models.Model):
    citation = models.CharField(max_length=400, blank=True, null=True)
    journals = models.ForeignKey('Journals', models.DO_NOTHING, db_column='journal_id', blank=True, null=True)
    # journal_id = models.IntegerField(blank=True, null=True)
    journal = models.CharField(max_length=128, blank=True, null=True)
    publisher = models.CharField(max_length=256, blank=True, null=True)
    abbrev = models.CharField(max_length=128, blank=True, null=True)
    authors = models.CharField(max_length=2048, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    volume = models.CharField(max_length=16, blank=True, null=True)
    issue = models.CharField(max_length=16, blank=True, null=True)
    startpage = models.CharField(max_length=6, blank=True, null=True)
    endpage = models.CharField(max_length=6, blank=True, null=True)
    title = models.CharField(max_length=1024, blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    doi = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=15)
    comments = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'references'


class ReferencesReports(models.Model):
    references = models.ForeignKey('References', models.DO_NOTHING, db_column='reference_id', blank=True, null=True)
    # reference_id = models.IntegerField(blank=True, null=True)
    reports = models.ForeignKey('Reports', models.DO_NOTHING, db_column='report_id', blank=True, null=True)
    # report_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=12)
    methodrefnum = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'references_reports'
        unique_together = (('references', 'reports'),)


class Reports(models.Model):
    volumes = models.ForeignKey('Volumes', models.DO_NOTHING, db_column='volume_id', blank=True, null=True)
    # volume_id = models.SmallIntegerField()
    page = models.CharField(max_length=8)
    systems = models.ForeignKey('Systems', models.DO_NOTHING, db_column='system_id', blank=True, null=True)
    # system_id = models.IntegerField()
    type = models.CharField(max_length=11)
    variables = models.CharField(max_length=512, blank=True, null=True)
    method = models.CharField(max_length=2048, blank=True, null=True)
    comments = models.CharField(max_length=1024)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reports'


class Substances(models.Model):
    casno = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    formula = models.CharField(max_length=1024, blank=True, null=True)
    formula_html = models.CharField(max_length=1024, blank=True, null=True)
    molweight = models.FloatField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'substances'


class SubstancesSystems(models.Model):
    substances = models.ForeignKey('Substances', models.DO_NOTHING, db_column='substance_id', blank=True, null=True)
    # substance_id = models.IntegerField(blank=True, null=True)
    systems = models.ForeignKey('Systems', models.DO_NOTHING, db_column='system_id', blank=True, null=True)
    # system_id = models.IntegerField(blank=True, null=True)
    compnum = models.CharField(max_length=9)
    role = models.CharField(max_length=9)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'substances_systems'


class Suppdata(models.Model):
    datapoint_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum_rownum = models.CharField(max_length=32, db_collation='utf8_general_ci')
    report_id = models.IntegerField(blank=True, null=True)
    dataset_id = models.IntegerField(blank=True, null=True)
    sysid = models.CharField(max_length=15, db_collation='utf8_general_ci')
    dataseries_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=15, db_collation='utf8_general_ci')
    source = models.CharField(max_length=10, db_collation='utf8_general_ci', blank=True, null=True)
    dataformat = models.CharField(max_length=5, db_collation='utf8_general_ci')
    property_id = models.IntegerField(blank=True, null=True)
    significand = models.TextField(db_collation='utf8_general_ci')
    exponent = models.TextField(db_collation='utf8_general_ci')
    error = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    error_type = models.CharField(max_length=8, db_collation='utf8_general_ci')
    number_of_observations = models.SmallIntegerField(db_column='number of observations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    unit_id = models.SmallIntegerField()
    accuracy = models.TextField(db_collation='utf8_general_ci')
    component = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    note = models.TextField(db_collation='utf8_general_ci')
    exact = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'suppdata'


class Systems(models.Model):
    name = models.CharField(max_length=256)
    volume_id = models.SmallIntegerField(blank=True, null=True)
    components = models.PositiveIntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'systems'


class Units(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    quantity_id = models.SmallIntegerField(blank=True, null=True)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=9)
    qudt = models.CharField(max_length=32, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'units'


class Users(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=128, db_collation='utf8_general_ci')
    firstname = models.CharField(max_length=16)
    lastname = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    type = models.CharField(max_length=10)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class Volumes(models.Model):
    id = models.SmallAutoField(primary_key=True)
    volume = models.CharField(max_length=32, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=512)
    url = models.CharField(max_length=128)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'volumes'
