""" example code for the substances app"""
import os
import django
import json
import collections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.models import *


data = Substances.objects.all().values('id', 'name')
chars = []
subs = {}
for s in data:
    first = s['name'][0].upper()
    if first not in subs.keys():
        subs.update({first: []})
        chars.append(first)
    subs[first].append(tuple((s['id'], s['name'])))
for char in chars:
    for sub in subs[char]:
        print(sub[0])
        exit()
