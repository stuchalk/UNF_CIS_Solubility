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
    list_display = ('id', 'title', 'description', 'report')
    ordering = ('id', 'title', 'report')
    search_fields = ('title', 'description', 'report')
    list_filter = ('report__volume__volume',)


@admin.register(Dataseries)
class DataseriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'seriesnum', 'dataset')
    ordering = ('heading', 'dataset')
    search_fields = ('dataset', 'heading',)
    list_filter = ('dataset__report__volume__volume',)


@admin.register(Datapoints)
class DatapointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dataset', 'dataseries')
    ordering = ('title', 'dataset', 'dataseries')
    search_fields = ('title',)
    list_filter = ('dataseries', 'dataset')


@admin.register(Quantities)
class QuantitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'baseunit')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'type')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Conditions)
class ConditionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_point', 'get_quantity', 'text', 'get_unit' )
    ordering = ('quantity__name', 'text',)
    search_fields = ('datapoint', 'text',)

    @display(ordering='quantity__name', description='Quantity')
    def get_quantity(self, obj):
        return obj.quantity.name

    @display(ordering='datapoint__title', description='Datapoint')
    def get_point(self, obj):
        return obj.datapoint.title

    @display(ordering='unit__name', description='Unit')
    def get_unit(self, obj):
        return obj.unit.name


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'text', 'unit', 'datapoint')
    ordering = ('id',)
    search_fields = ('datapoint', 'quantity',)
