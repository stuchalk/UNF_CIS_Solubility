""" app config for sds DB """
from django.apps import AppConfig


class SystemsConfig(AppConfig):
    """config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'systems'
