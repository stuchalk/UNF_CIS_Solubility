from django.contrib import admin
from sds.models import Reports


@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('id', 'volume', 'system', 'type', 'page')
    ordering = ('volume__vol', 'system__name', 'page')
    search_fields = ('volume__vol', 'page', 'system__name')
    list_filter = ('volume__vol',)
