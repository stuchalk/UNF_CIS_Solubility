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
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authors(models.Model):
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
    id = models.SmallAutoField(primary_key=True)
    author_id = models.SmallIntegerField()
    report_id = models.IntegerField()
    name = models.CharField(max_length=255)
    sysid = models.CharField(max_length=20)
    role = models.CharField(max_length=9)
    order = models.PositiveIntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authors_reports'


class Chemicals(models.Model):
    description = models.TextField(blank=True, null=True)
    substance_id = models.IntegerField()
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


class Classes(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    identifier = models.CharField(max_length=7)
    expression = models.CharField(max_length=32)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'classes'


class Conditions(models.Model):
    datapoint_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum_rownum = models.CharField(max_length=32, blank=True, null=True)
    dataseries_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=15, blank=True, null=True)
    property_id = models.IntegerField()
    significand = models.CharField(max_length=16)
    exponent = models.IntegerField()
    error = models.CharField(max_length=16, blank=True, null=True)
    error_type = models.CharField(max_length=8, blank=True, null=True)
    unit_id = models.SmallIntegerField()
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
    datapoint_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum_rownum = models.CharField(max_length=32)
    str_property = models.CharField(max_length=512)
    dataset_id = models.IntegerField(blank=True, null=True)
    dataseries_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=15)
    property_id = models.IntegerField(blank=True, null=True)
    dataformat = models.CharField(max_length=5)
    significand = models.TextField()
    exponent = models.TextField()
    error = models.TextField()
    error_type = models.CharField(max_length=8)
    unit_id = models.SmallIntegerField()
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
    dataset_id = models.IntegerField(blank=True, null=True)
    dataseries_id = models.IntegerField(blank=True, null=True)
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
    id = models.SmallAutoField(primary_key=True)
    dataset_id = models.IntegerField()
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
    sysid = models.CharField(max_length=10)
    sysnmid = models.PositiveIntegerField()
    report_id = models.IntegerField()
    system_id = models.IntegerField()
    reference_id = models.IntegerField()
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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Errorbars(models.Model):
    dataset_id = models.IntegerField(blank=True, null=True)
    sysid = models.CharField(max_length=50, blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=128, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)
    unit_id = models.SmallIntegerField(blank=True, null=True)
    raw = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'errorbars'


class Errors(models.Model):
    dataset_id = models.IntegerField(blank=True, null=True)
    sysid = models.CharField(max_length=50, blank=True, null=True)
    property_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=128, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)
    unit_id = models.SmallIntegerField(blank=True, null=True)
    raw = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'errors'


class Evaluations(models.Model):
    id = models.SmallAutoField(primary_key=True)
    evalid = models.CharField(max_length=10, blank=True, null=True)
    report_id = models.IntegerField()
    title = models.CharField(max_length=256)
    raw = models.TextField(blank=True, null=True)
    sysid = models.CharField(max_length=10, blank=True, null=True)
    data = models.IntegerField()
    date = models.CharField(max_length=64, blank=True, null=True)
    updated = models.IntegerField()

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


class Figures(models.Model):
    id = models.SmallAutoField(primary_key=True)
    caption = models.CharField(max_length=256, blank=True, null=True)
    sysid = models.CharField(max_length=15, blank=True, null=True)
    report_id = models.IntegerField()
    number = models.IntegerField()
    location = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'figures'


class Footnotes(models.Model):
    id = models.SmallAutoField(primary_key=True)
    report_id = models.IntegerField()
    sysid = models.CharField(max_length=8)
    note = models.CharField(max_length=8, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    tablenum = models.PositiveIntegerField(blank=True, null=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'footnotes'


class Identifiers(models.Model):
    substance_id = models.IntegerField()
    type = models.CharField(max_length=12)
    value = models.CharField(max_length=1024)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'identifiers'


class Properties(models.Model):
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=32)
    definition = models.CharField(max_length=512)
    source = models.CharField(max_length=256)
    unit_id = models.SmallIntegerField()
    quantity_id = models.SmallIntegerField(blank=True, null=True)
    field = models.CharField(max_length=256)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'properties'


class Publications(models.Model):
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


class Quantities(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    symbol = models.CharField(max_length=8)
    description = models.CharField(max_length=512)
    si_unit = models.SmallIntegerField()
    dim_symbol = models.CharField(max_length=16)
    comment = models.CharField(max_length=512)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quantities'


class ReferenceLst(models.Model):
    id = models.SmallAutoField(primary_key=True)
    reference_id = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    pub_year = models.CharField(max_length=50, blank=True, null=True)
    doi = models.CharField(db_column='DOI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(db_column='SCORE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reference_lst'


class References(models.Model):
    refid = models.IntegerField(blank=True, null=True)
    report_id = models.IntegerField(blank=True, null=True)
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


class ReferencesReports(models.Model):
    reference_id = models.IntegerField(blank=True, null=True)
    report_id = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=12, blank=True, null=True)
    reference_num = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'references_reports'
        unique_together = (('reference_id', 'report_id'),)


class Reports(models.Model):
    publication_id = models.SmallIntegerField()
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
    substance_id = models.IntegerField(blank=True, null=True)
    system_id = models.IntegerField(blank=True, null=True)
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


class Suppdata(models.Model):
    datapoint_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum_rownum = models.CharField(max_length=32)
    report_id = models.IntegerField(blank=True, null=True)
    dataset_id = models.IntegerField(blank=True, null=True)
    sysid = models.CharField(max_length=15)
    dataseries_id = models.IntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=15)
    source = models.CharField(max_length=10, blank=True, null=True)
    dataformat = models.CharField(max_length=5)
    property_id = models.IntegerField(blank=True, null=True)
    significand = models.TextField()
    exponent = models.TextField()
    error = models.TextField(blank=True, null=True)
    error_type = models.CharField(max_length=8)
    number_of_observations = models.SmallIntegerField(db_column='number of observations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    unit_id = models.SmallIntegerField()
    accuracy = models.TextField()
    component = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    note = models.TextField()
    exact = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'suppdata'


class Systems(models.Model):
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


class Units(models.Model):
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


class Users(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=1024)
    firstname = models.CharField(max_length=16)
    lastname = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    type = models.CharField(max_length=10)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class Variables(models.Model):
    id = models.SmallAutoField(primary_key=True)
    report_id = models.IntegerField()
    sysid = models.CharField(max_length=32)
    property = models.CharField(max_length=5, blank=True, null=True)
    value = models.CharField(max_length=255)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'variables'
