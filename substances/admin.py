from django.contrib import admin
from sds.models import Substances
from sds.models import Identifiers
from sds.models import Chemicals


@admin.register(Substances)
class SubstancesAdmin(admin.ModelAdmin):
    list_display = ('name', 'formula', 'casno')
    ordering = ('name',)
    search_fields = ('name', 'formula')


@admin.register(Identifiers)
class IdentifiersAdmin(admin.ModelAdmin):
    list_display = ('type', 'value')
    ordering = ('value',)
    search_fields = ('type', 'value')
    list_filter = ('substance',)


@admin.register(Chemicals)
class ChemicalsAdmin(admin.ModelAdmin):
    list_display = ('substance', 'report')
    ordering = ('substance',)
    search_fields = ('substance', 'report')
