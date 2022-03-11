""" example code for the substances app"""
import os
import django
import json
import collections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.models import *

refid = 703
ref = References.objects.get(id=refid)
rprtids = ReferencesReports.objects.all().filter(reference_id=refid).values_list('report_id', flat=True)
print(rprtids)
exit()
