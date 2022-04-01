import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.serializers import *
import json


rep = Reports.objects.get(id=1)
report = ReportSerializer(rep)
data = report.data
sys = data['system']
vol = data['volume']
sysid = sys['id']
dset = data['set']
print(dset)
exit()
