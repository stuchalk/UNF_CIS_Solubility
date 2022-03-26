""" example code for the systems app"""
import os
import django
import json
import collections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()

from django.db.models.functions import *
from sds.models import *
from sds.functions import *

""" show data about a specific system """
sys = Systems.objects.get(id=1)
print(sys)
# substances that the system is part of
subids = sys.substancessystems_set.values('substance_id')
print(subids)
subs = Substances.objects.all().filter(id__in=subids, identifiers__type='inchikey'). \
    values_list('id', 'identifiers__value')
print(subs)
exit()