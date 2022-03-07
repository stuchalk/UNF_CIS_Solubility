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
# syss = Systems.objects.annotate(first=Upper(Substr('name', 1, 1)))
syss = Systems.objects.all().values('id', 'name').order_by('name').annotate(first=Upper(Substr('name', 1, 1)))
lst = list(syss)
olst = groupbyfirst(lst)
# srtd = collections.OrderedDict(sorted(olst.items()))
print(olst)
exit()
