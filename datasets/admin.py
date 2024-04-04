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
from sds.models import Suppdata


@admin.register(Datasets)
class DatasetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'report')
    ordering = ('title', 'report')
    search_fields = ('dataset_title', 'description', 'report')
    list_filter = ('report__volume__volume',)


@admin.register(Dataseries)
class DataseriesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'seriesnum', 'dataset')
    ordering = ('dataset', 'heading')
    search_fields = ('dataset__title', 'dataseries__heading',)


@admin.register(Datapoints)
class DatapointsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_set', 'get_series')
    ordering = ('title', 'dataset', 'dataseries')
    search_fields = ('dataseries__heading', 'dataseries__dataset__title',)
    autocomplete_fields = ('dataseries', 'dataset',)

    @display(ordering='dataseries__heading', description='Dataseries')
    def get_series(self, obj):
        """ series heading """
        return obj.dataseries.heading

    @display(ordering='dataseries__dataset__title', description='Dataset')
    def get_set(self, obj):
        """ series heading """
        return obj.dataseries.dataset.title


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
    list_display = ('get_point', 'get_series', 'get_quantity', 'text', 'get_unit')
    ordering = ('quantity__name', 'text',)
    search_fields = ('datapoint__title', 'datapoint__dataseries__heading', 'text',)
    autocomplete_fields = ('datapoint', 'dataseries')

    @display(ordering='quantity__name', description='Quantity')
    def get_quantity(self, obj):
        """ quantity name """
        return obj.quantity.name

    @display(ordering='datapoint__dataseries__heading', description='Dataseries')
    def get_series(self, obj):
        """ series heading """
        return obj.datapoint.dataseries.heading

    @display(ordering='datapoint__title', description='Datapoint')
    def get_point(self, obj):
        """ datapoint title """
        return obj.datapoint.title

    @display(ordering='unit__symbol', description='Unit')
    def get_unit(self, obj):
        """ unit symbol """
        return obj.unit.symbol


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('get_point', 'quantity', 'text', 'unit', 'compnum')
    ordering = ('id',)
    search_fields = ('datapoint__title', 'quantity__name',
                     'datapoint__dataseries__heading', 'datapoint__dataseries__dataset__title')
    autocomplete_fields = ('datapoint',)

    @display(ordering='datapoint__title', description='Datapoint')
    def get_point(self, obj):
        """ datapoint title """
        return obj.datapoint.title


@admin.register(Suppdata)
class SuppdataAdmin(admin.ModelAdmin):
    list_display = ('get_point', 'quantity', 'text', 'unit', 'compnum')
    ordering = ('id',)
    search_fields = ('datapoint__title', 'quantity__name',
                     'datapoint__dataseries__heading', 'datapoint__dataseries__dataset__title')
    autocomplete_fields = ('datapoint',)

    @display(ordering='datapoint__title', description='Datapoint')
    def get_point(self, obj):
        """ datapoint title """
        return obj.datapoint.title
