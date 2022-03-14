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
rrptids = ReferencesReports.objects.all().filter(reference_id=refid).values_list('report_id', flat=True)
rdsets = Datasets.objects.all().filter(report_id__in=rrptids).values('report_id', 'system__name')
evalids = EvaluationsReferences.objects.all().filter(reference_id=refid).values_list('evaluation_id', flat=True)
erptids = Evaluations.objects.all().filter(id__in=evalids).values_list('report_id', flat=True)
edsets = Datasets.objects.all().filter(id__in=erptids).values('report_id', 'system__name')
print(rdsets)
print(edsets)
exit()
