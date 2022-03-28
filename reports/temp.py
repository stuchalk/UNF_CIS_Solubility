import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.serializers import *
import json


rep = Reports.objects.get(id=1)
report = ReportSerializer(rep)
print(json.dumps(report.data, indent=4))
exit()
