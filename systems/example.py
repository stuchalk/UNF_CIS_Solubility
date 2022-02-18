""" example code for the datafiles app"""
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()

from django.db.models.functions import *
from systems.models import *

# syss = Systems.objects.annotate(first=Upper(Substr('name', 1, 1)))
syss = Systems.objects.all().values().
print(json.dumps(dict(syss), indent=2))
exit()
