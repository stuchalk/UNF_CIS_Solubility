from django.contrib import admin
from sds.models import References
from sds.models import ReferencesReports


@admin.register(References)
class ReferencesAdmin(admin.ModelAdmin):
    list_display = ('journal', 'year', 'volume', 'startpage', 'doi')
    ordering = ('journal', 'year')
    search_fields = ('journal', 'doi')


@admin.register(ReferencesReports)
class ReferencesReportsAdmin(admin.ModelAdmin):
    list_display = ('reference', 'report', 'type')
    ordering = ('reference', 'report')
    search_fields = ('report', 'type')
