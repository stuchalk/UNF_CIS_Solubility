""" django models file for reports app """
from django.db import models
from django.utils.translation import gettext_lazy as _


class Authors(models.Model):
    """ authors table model """
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    abbrev = models.CharField(max_length=128, blank=True, null=True)
    institution = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    orcid = models.CharField(max_length=20, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'authors'
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.name}"


class AuthorsReports(models.Model):
    """ authors_reports table model """

    class RoleOpts(models.TextChoices):
        """ component options enum list """
        EV = ('evaluator', _('Critical evaluator'))
        CM = ('compiler', _('Compiler'))

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey("Authors", models.DO_NOTHING, db_column="author_id")
    report = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    role = models.CharField(max_length=9, choices=RoleOpts.choices, default='compiler')
    order = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'authors_reports'
        verbose_name_plural = "authors/reports (join)"

    def __str__(self):
        return f"{self.author.name} - Vol. {self.report.vol}, page {self.report.page}"


class Chemicals(models.Model):
    """ chemicals table model """
    id = models.AutoField(primary_key=True)
    substance = models.ForeignKey("Substances", models.DO_NOTHING, db_column="substance_id")
    report = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    supplier = models.CharField(max_length=128, blank=True, null=True)
    purity = models.CharField(max_length=128, blank=True, null=True)
    compnum = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'chemicals'
        verbose_name_plural = "chemicals"

    def __str__(self):
        return f'{self.substance.name} - Vol. {self.report.vol.volume}, page {self.report.page}'


class Conditions(models.Model):
    """ conditions table model """
    id = models.AutoField(primary_key=True)
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
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'conditions'


class Data(models.Model):
    """ data table model """
    id = models.AutoField(primary_key=True)
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
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'data'


class Datapoints(models.Model):
    """ datapoints table model """
    id = models.AutoField(primary_key=True)
    dataset = models.ForeignKey("Datasets", models.DO_NOTHING, db_column="dataset_id")
    dataseries = models.ForeignKey("Dataseries", models.DO_NOTHING, db_column="dataseries_id")
    sysid = models.CharField(max_length=15, blank=True, null=True)
    tablenum = models.SmallIntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=10, blank=True, null=True)
    sysid_tablenum_rownum = models.CharField(max_length=32, blank=True, null=True)
    rownum = models.SmallIntegerField(blank=True, null=True)
    row_index = models.SmallIntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'datapoints'


class Dataseries(models.Model):
    """ dataseries table model """
    id = models.AutoField(primary_key=True)
    dataset = models.ForeignKey("Datasets", models.DO_NOTHING, db_column="dataset_id")
    sysid = models.CharField(max_length=15, blank=True, null=True)
    tablenum = models.SmallIntegerField(blank=True, null=True)
    sysid_tablenum = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20)
    heading = models.CharField(max_length=512)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'dataseries'


class Datasets(models.Model):
    """ datasets table model """
    id = models.AutoField(primary_key=True)
    sysid = models.CharField(max_length=10)
    sysnmid = models.PositiveIntegerField()
    report = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    reference = models.ForeignKey("References", models.DO_NOTHING, db_column="reference_id")
    system = models.ForeignKey("Systems", models.DO_NOTHING, db_column="system_id")
    eval = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=256, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'datasets'


class Evaluations(models.Model):
    """ evaluations table model """
    id = models.SmallAutoField(primary_key=True)
    evalid = models.CharField(max_length=10, db_collation='utf8_general_ci', blank=True, null=True)
    report_id = models.IntegerField()
    title = models.CharField(max_length=256)
    raw = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    sysid = models.CharField(max_length=10, db_collation='utf8_general_ci', blank=True, null=True)
    data = models.IntegerField()
    date = models.CharField(max_length=64, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'evaluations'


class EvaluationsReferences(models.Model):
    """ evaluations_references table model """
    id = models.AutoField(primary_key=True)
    evaluation_id = models.SmallIntegerField(blank=True, null=True)
    evalid = models.CharField(max_length=50, blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    refid = models.CharField(max_length=50, blank=True, null=True)
    citenum = models.CharField(max_length=8, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'evaluations_references'


class Identifiers(models.Model):
    """ indentifiers table model """
    # reference types enum list
    ISTR = 'inchi'
    IKEY = 'inchikey'
    CSML = 'smiles'
    TYPE_CHOICES = [
        (ISTR, 'InChI'),
        (IKEY, 'InChIKey'),
        (CSML, 'Canonical SMILES')
    ]
    id = models.AutoField(primary_key=True)
    substance = models.ForeignKey("Substances", models.DO_NOTHING, db_column="substance_id")
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, default=ISTR)
    value = models.CharField(max_length=1024)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'identifiers'
        verbose_name_plural = "identifiers"

    def __str__(self):
        return f'{self.type} ({self.substance.name})'


class Properties(models.Model):
    """ properties table model """
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=256, db_collation='utf8_general_ci')
    symbol = models.CharField(max_length=64, db_collation='utf8_general_ci')
    datafield = models.CharField(max_length=255, blank=True, null=True)
    definition = models.CharField(max_length=512, db_collation='utf8_general_ci')
    source = models.CharField(max_length=256, db_collation='utf8_general_ci')
    quantity = models.ForeignKey("Quantities", models.DO_NOTHING, db_column="quantity_id")
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'properties'


class Quantities(models.Model):
    """ quantities table model """
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=32, db_collation='utf8_general_ci')
    symbol = models.CharField(max_length=8, db_collation='utf8_general_ci')
    description = models.CharField(max_length=512, db_collation='utf8_general_ci')
    siunit = models.ForeignKey("Units", models.DO_NOTHING, db_column="si_unit")
    dim_symbol = models.CharField(max_length=16, db_collation='utf8_general_ci')
    comment = models.CharField(max_length=512, db_collation='utf8_general_ci')
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'quantities'


class References(models.Model):
    """ references model """

    class RefTypes(models.TextChoices):
        """ reference types enum list """
        JART = 'paper', _('Journal article')
        BOOK = 'book', _('Book')
        DISS = 'dissertation', _('Dissertation')
        THES = 'thesis', _('Thesis')
        REPT = 'report', _('Report')
        COMM = 'communication', _('Communication')
        CHAP = 'chapter', _('Book Chapter')
        PATN = 'patent', _('Patent')

    # fields
    id = models.AutoField(primary_key=True)
    raw = models.TextField(blank=True, null=True)
    journal = models.CharField(max_length=128, blank=True, null=True)
    publisher = models.CharField(max_length=256, blank=True, null=True)
    abbrev = models.CharField(max_length=128, blank=True, null=True)
    authors = models.CharField(max_length=2048, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    volume = models.CharField(max_length=6, blank=True, null=True)
    issue = models.CharField(max_length=16, blank=True, null=True)
    startpage = models.CharField(max_length=6, blank=True, null=True)
    endpage = models.CharField(max_length=6, blank=True, null=True)
    title = models.CharField(max_length=1024, blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    doi = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=15, choices=RefTypes.choices, default='paper')
    comments = models.CharField(max_length=512, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'references'
        verbose_name_plural = "references"

    def __str__(self):
        return f"{self.raw}"


class Reports(models.Model):
    """ reports table model """

    class TypeOpts(models.TextChoices):
        """ component options enum list """
        EV = ('evaluation', _('System evaluation'))
        CM = ('compilation', _('Compilation'))

    id = models.AutoField(primary_key=True)
    vol = models.ForeignKey("Volumes", models.DO_NOTHING, db_column="volume_id")
    page = models.CharField(max_length=8)
    sys = models.ForeignKey("Systems", models.DO_NOTHING, db_column="system_id")
    type = models.CharField(max_length=11, choices=TypeOpts.choices, default='compilation')
    variables = models.CharField(max_length=512, blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=1024)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'reports'
        verbose_name_plural = "reports"

    def __str__(self):
        return f'{self.sys.name} (Vol. {self.vol.volume}, page {self.page})'


class ReferencesReports(models.Model):
    """ reports references_reports join table model """

    class TypeOpts(models.TextChoices):
        """ component options enum list """
        EV = ('original', _('Original Measurements Paper'))
        CM = ('supplmental', _('Method Reference Paper'))

    id = models.AutoField(primary_key=True)
    reference = models.ForeignKey("References", models.DO_NOTHING, db_column="reference_id")
    report = models.ForeignKey("Reports", models.DO_NOTHING, db_column="report_id")
    type = models.CharField(max_length=12, choices=TypeOpts.choices, default='original')
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'references_reports'
        verbose_name_plural = "refs/reports (join)"

    def __str__(self):
        return f"{self.reference.raw} - Vol. {self.report.vol}, page {self.report.page}"


class Substances(models.Model):
    """ substances table model """
    id = models.AutoField(primary_key=True)
    casno = models.CharField(max_length=50, blank=True, null=True, unique=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    formula = models.CharField(max_length=1024, blank=True, null=True)
    formula_html = models.CharField(max_length=1024, blank=True, null=True)
    molweight = models.FloatField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'substances'
        verbose_name_plural = "substances"

    def __str__(self):
        return f"{self.name}"


class SubstancesSystems(models.Model):
    """ substances_systems table model """

    class CompNums(models.TextChoices):
        """ component number options enum list """
        UND = 'undefined', _('Change me!')
        ONE = '1', _('Component 1')
        TWO = '2', _('Component 2')
        THR = '3', _('Component 3')
        FOR = '4', _('Component 4')

    class Roles(models.TextChoices):
        """ role options enum list """
        UND = 'undefined', _('Change me!')
        SOL = 'solute', _('Solute')
        SVT = 'solvent', _('Solvent')
        MUT = 'mutual', _('Mutual solubility')

    # fields
    id = models.AutoField(primary_key=True)
    substance = models.ForeignKey("Substances", models.DO_NOTHING, db_column="substance_id")
    system = models.ForeignKey("Systems", models.DO_NOTHING, db_column="system_id")
    compnum = models.CharField(max_length=9, choices=CompNums.choices, default='undefined')
    role = models.CharField(max_length=9, choices=Roles.choices, default='undefined')
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'substances_systems'
        verbose_name_plural = "subs/systems (join)"

    def __str__(self):
        return f'{self.system.name} ({self.role})'


class Systems(models.Model):
    """ systems table model """

    class CompOpts(models.IntegerChoices):
        """ component options enum list """
        BIN = (2, _('Binary mixture'))
        TER = (3, _('Ternary mixture'))
        QTN = (4, _('Quaternary mixture'))

    # fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, db_collation='utf8_general_ci')
    vol = models.ForeignKey("Volumes", models.DO_NOTHING, db_column="volume_id")
    components = models.PositiveIntegerField(choices=CompOpts.choices, default=2)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'systems'
        verbose_name_plural = "systems"

    def __str__(self):
        return f"{self.name}"


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
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'units'


class Volumes(models.Model):
    """ publications table model """
    id = models.SmallAutoField(primary_key=True)
    volume = models.CharField(max_length=32, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=256)
    authors = models.CharField(max_length=512)
    url = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'volumes'
        verbose_name_plural = "volumes"

    def __str__(self):
        return f"{self.volume}"
