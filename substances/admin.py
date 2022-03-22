from django.contrib import admin
from sds.models import Substances
from sds.models import Identifiers


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
