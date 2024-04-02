from django.contrib import admin
from sds.models import References
from sds.models import ReferencesReports
from sds.models import Journals


@admin.register(References)
class ReferencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'volume', 'startpage', 'doi')
    ordering = ('citation', 'title')
    search_fields = ('title', 'doi')
    list_filter = ('journal__abbrev',)


@admin.register(ReferencesReports)
class ReferencesReportsAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'report', 'type')
    ordering = ('reference__citation', 'report')
    search_fields = ('report', 'type')


@admin.register(Journals)
class JournalsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abbrev', 'publisher')
    ordering = ('name', )
    search_fields = ('name', 'publisher')
