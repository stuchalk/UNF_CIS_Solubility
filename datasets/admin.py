from django.contrib import admin
from sds.models import Datasets
from sds.models import Dataseries
from sds.models import Datapoints
from sds.models import Conditions
from sds.models import Data


@admin.register(Datasets)
class DatasetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'report')
    ordering = ('title', 'report')
    search_fields = ('title', 'description')
