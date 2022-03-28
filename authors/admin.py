from django.contrib import admin
from sds.models import Authors
from sds.models import AuthorsReports


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'email')
    ordering = ('name', 'institution')
    search_fields = ('name', 'institution', 'email')


@admin.register(AuthorsReports)
class AuthorsReportsAdmin(admin.ModelAdmin):
    list_display = ('author', 'role', 'report')
    ordering = ('author', 'report')
    search_fields = ('author', 'report')
