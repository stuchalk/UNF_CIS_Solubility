from django.contrib import admin
from sds.models import Reports


@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('vol', 'sys', 'type', 'page')
    ordering = ('vol', 'sys', 'page')
    search_fields = ('vol', 'type', 'page')
