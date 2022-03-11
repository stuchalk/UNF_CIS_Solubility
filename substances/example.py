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
syss = Systems.objects.all().filter(id__in=subids).values_list('id', 'name').order_by('name')
sysids = Systems.objects.all().filter(id__in=subids).values_list('id', flat=True).order_by('name')

print(sysids)
exit()

idlist = {}
print(ids)
for idtype, value in ids:
    if idtype not in idlist.keys():
        idlist.update({idtype: []})
    idlist[idtype].append(value)
print(idlist)
