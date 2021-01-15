""" django unit test file"""
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from reports.serializers import *
from scidata.model import *
from datetime import datetime
sysid = '58_1'
rep = Reports.objects.get(sysid__exact=sysid)
report = ReportSerializer(rep)
data = report.data
# print(json.dumps(data, indent=4))
# exit()

# organize data
pub = data['pub']
dst = data['set']
ref = dst[0]['reference']


# create json-ld file
test = SciData(sysid)
test.context(['https://stuchalk.github.io/scidata/contexts/sds.jsonld',
              'https://stuchalk.github.io/scidata/contexts/scidata.jsonld'])
test.add_namespace({'w3i': 'https://w3id.org/skgo/modsci#'})
test.base({"@base": "https://scidata.unf.edu/iupac/sds/" + sysid + "/"})
test.version(1)
test.generatedAt(str(datetime.now()))
test.publisher('The International Union of Pure and Applied Chemistry')
test.add_keyword('Solubility')
test.add_keyword('Solubility data series')
test.title('Solubility data from volume ' + pub['volume'])
test.discipline('w3i:Chemistry')
test.subdiscipline('w3i:PhysicalChemistry')

test.add_source([{"title": pub['title'], "year": pub['year'], "type": "Critically evaluate report"}])
if ref:
    test.add_source([{"title": ref['title'], "year": ref['year'], "type": "Journal article", "doi": ref['doi']}])
test.rights("https://creativecommons.org/licenses/by-nc/4.0/", "NIST & IUPAC")
output = test.output

print(json.dumps(output, indent=4))
