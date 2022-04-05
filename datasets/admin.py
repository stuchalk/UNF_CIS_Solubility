""" admin setup for datasets """
from django.contrib import admin
from django.contrib.admin import display
from sds.models import Datasets
from sds.models import Dataseries
from sds.models import Datapoints
from sds.models import Quantities
from sds.models import Units
from sds.models import Conditions
from sds.models import Data


@admin.register(Datasets)
class DatasetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'report')
    ordering = ('title', 'report')
    search_fields = ('title', 'description')


@admin.register(Dataseries)
class DataseriesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'seriesnum', 'dataset')
    ordering = ('heading', 'dataset')
    search_fields = ('heading',)


@admin.register(Datapoints)
class DatapointsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dataset', 'dataseries')
    ordering = ('dataset', 'dataseries')
    search_fields = ('title',)
    list_filter = ('dataseries','dataset')


@admin.register(Quantities)
class QuantitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'baseunit')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'type')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Conditions)
class ConditionsAdmin(admin.ModelAdmin):
    list_display = ('datapoint_id', 'get_name', 'text')
    ordering = ('datapoint_id',)
    search_fields = ('get_name',)

    @display(ordering='quantity__name', description='Name')
    def get_name(self, obj):
        return obj.quantity.name

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'text', 'unit', 'datapoint')
    ordering = ('quantity',)
    search_fields = ('quantity',)
