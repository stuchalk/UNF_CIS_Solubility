from django.contrib import admin
from sds.models import Reports


@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('id', 'volume', 'system', 'type', 'page')
    ordering = ('id', 'volume', 'system', 'page')
    search_fields = ('id', 'volume__volume', 'type', 'page')
    list_filter = ('volume',)
