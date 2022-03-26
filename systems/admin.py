""" admin setup for systems """
from django.contrib import admin
from sds.models import Systems
from sds.models import SubstancesSystems


@admin.register(Systems)
class SystemsAdmin(admin.ModelAdmin):
    """ systems table admin config """
    list_display = ('name', 'components', 'vol')
    ordering = ('name',)
    search_fields = ('name', 'vol')


@admin.register(SubstancesSystems)
class SubstancesSystemsAdmin(admin.ModelAdmin):
    """ substances_systems table admin config """
    list_display = ('system', 'substance', 'role')
    ordering = ('system',)
    search_fields = ('system', 'substance')
