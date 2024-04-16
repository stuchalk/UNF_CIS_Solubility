from django.contrib import admin
from sds.models import Volumes


@admin.register(Volumes)
class VolumesAdmin(admin.ModelAdmin):
    list_display = ('vol', 'year', 'title')
    ordering = ('vol',)
    search_fields = ('title', 'vol')
