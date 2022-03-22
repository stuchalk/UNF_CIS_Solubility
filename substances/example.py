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
syslst = Systems.objects.all().filter(id__in=sysids).values('id', 'name').order_by('name')
rrpts = Datasets.objects.all().filter(system__in=sysids, eval=0).values('system_id', 'report_id', 'report__referencesreports__reference__raw')
erpts = Datasets.objects.all().filter(system__in=sysids, eval=1).values('system_id', 'report_id')
syss = {}
for sys in syslst:
    if sys['id'] not in syss.keys():
        syss.update({sys['id']: []})
    syss[sys['id']].append(sys['name'])
    elst = []
    for erpt in erpts:
        if erpt['system_id'] == sys['id']:
            elst.append(erpt['report_id'])
    syss[sys['id']].append(elst)
    rlst = []
    for rrpt in rrpts:
        if rrpt['system_id'] == sys['id']:
            rlst.append(tuple((rrpt['report_id'], rrpt['report__referencesreports__reference__raw'])))
    syss[sys['id']].append(rlst)
print(syss)
