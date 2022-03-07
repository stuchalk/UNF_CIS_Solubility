""" example code for the substances app"""
import os
import django
import json
import collections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.models import *

sub = Substances.objects.get(id=1)
ids = sub.identifiers_set.values_list('type', 'value')
subids = sub.substancessystems_set.values_list('system_id', flat=True).distinct()
print(subids)
exit()

syss = Systems.objects.filter(id=subids)

print(syss)
exit()
idlist = {}
print(ids)
for idtype, value in ids:
    if idtype not in idlist.keys():
        idlist.update({idtype: []})
    idlist[idtype].append(value)
print(idlist)
