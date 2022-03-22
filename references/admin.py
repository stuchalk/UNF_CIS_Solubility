from django.contrib import admin
from sds.models import References


@admin.register(References)
class SubstancesAdmin(admin.ModelAdmin):
    list_display = ('journal', 'year', 'volume', 'startpage', 'doi')
    ordering = ('journal', 'year')
    search_fields = ('journal', 'doi')
