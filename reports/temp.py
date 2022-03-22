import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from sds.serializers import *
import json


repid = 3459
rep = Reports.objects.get(id__exact=repid)
data = ReportSerializer(rep).data
sysid = data['sysid']
sys = data['set'][0]['system']
subs = []
for temp in sys['subsys']:
    if temp['sysid'] == sysid:
        sub = temp['substance']
        for ident in sub['identifier']:
            sub.update({ident['type']: ident['value']})
        del sub['identifier']
        subs.append(sub)

print(json.dumps(data, indent=4))
exit()
