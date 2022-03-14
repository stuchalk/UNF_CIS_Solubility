""" example code for the substances app"""
import os
import django
import json
import collections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.models import *

sub = Substances.objects.get(id=293)
idents = sub.identifiers_set.values('type', 'value')
ids = {}
for id in idents:
    if id['type'] not in ids.keys():
        ids[id['type']] = id['value']
    else:
        ids[id['type']] += ", " + id['value']
sysids = sub.substancessystems_set.values_list('system_id', flat=True).distinct()
print(ids)
syss = Systems.objects.all().filter(id__in=sysids).values_list('id', 'name').order_by('name')
rrpts = Datasets.objects.all().filter(system__in=sysids, eval=0).values('report_id', 'system_id', 'report__referencesreports__reference__raw')
erpts = Datasets.objects.all().filter(system__in=sysids, eval=1).values('report_id', 'system_id')
rrptsbysys = {}
for rpt in rrpts:
    if rpt['system_id'] not in rrptsbysys.keys():
        rrptsbysys.update({rpt['system_id']: {}})
    rrptsbysys[rpt['system_id']].update({rpt['report_id']: rpt['report__referencesreports__reference__raw']})
erptsbysys = {}
for rpt in erpts:
    erptsbysys.update({rpt['system_id']: rpt['report_id']})
print(rrptsbysys)
print(erptsbysys)
exit()

idlist = {}
print(ids)
for idtype, value in ids:
    if idtype not in idlist.keys():
        idlist.update({idtype: []})
    idlist[idtype].append(value)
print(idlist)
