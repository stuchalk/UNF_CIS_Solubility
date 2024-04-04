from django.contrib import admin
from sds.models import Authors
from sds.models import AuthorsReports


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'institution', 'email')
    ordering = ('id', 'name', 'institution')
    search_fields = ('name', 'institution', 'email')


@admin.register(AuthorsReports)
class AuthorsReportsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'role', 'report')
    ordering = ('author', 'report')
    search_fields = ('author', 'report')
    autocomplete_fields = ('report',)
