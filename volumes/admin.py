from django.contrib import admin
from sds.models import Volumes


@admin.register(Volumes)
class VolumesAdmin(admin.ModelAdmin):
    list_display = ('id', 'volume', 'year', 'title')
    ordering = ('volume',)
    search_fields = ('title',)
