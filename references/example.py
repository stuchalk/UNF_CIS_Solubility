""" example code for the substances app"""
import os
import django
import json
import collections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.models import *

refs = References.objects.all().values_list('id', 'raw')
print(refs)
exit()
