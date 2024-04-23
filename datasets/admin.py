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
    list_display = ('id', 'title', 'description', 'report_id', 'report')
    ordering = ('title', 'report')
    search_fields = ('title', 'description', 'report__system__name')
    list_filter = ('report__volume__vol',)


@admin.register(Dataseries)
class DataseriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'seriesnum', 'dataset')
    ordering = ('dataset', 'heading')
    search_fields = ('heading', 'dataset__title', 'dataset__report__system__name')


@admin.register(Datapoints)
class DatapointsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_set', 'get_series')
    ordering = ('title', 'dataset', 'dataseries')
    search_fields = ('title', 'dataseries__heading')
    autocomplete_fields = ['dataseries', 'dataset']
    list_filter = ('dataseries__heading',)

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
    ordering = ('id', 'quantity__name', 'text',)
    search_fields = ['datapoint__dataseries__heading', 'datapoint__title', 'text']
    autocomplete_fields = ['dataseries', 'datapoint']
    list_filter = ('dataseries__heading',)

    @display(ordering='quantity__name', description='Quantity')
    def get_quantity(self, obj):
        """ quantity name """
        return obj.quantity.name

    @display(ordering='datapoint__dataseries__heading', description='Dataseries')
    def get_series(self, obj):
        """ series heading """
        if obj.datapoint is not None:
            return obj.datapoint.dataseries.heading
        else:
            return obj.dataseries.heading

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
