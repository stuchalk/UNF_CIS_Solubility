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


@admin.register(Datapoints)
class DatapointsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dataset', 'dataseries')
    ordering = ('dataset', 'dataseries')
    search_fields = ('title', )
