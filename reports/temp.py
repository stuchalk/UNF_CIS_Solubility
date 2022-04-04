import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.serializers import *
import json


rep = Reports.objects.get(id=88)
report = ReportSerializer(rep)
data = report.data
sys = data['system']
vol = data['volume']
sysid = sys['id']
dset = data['set']
series = dset[0]['dataseries']
points = dset[0]['datapoints']
print(series)
print(points)
exit()
