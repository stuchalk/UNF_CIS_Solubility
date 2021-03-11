""" django unit test file"""
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()
from reports.serializers import *
from SciDataLib.SciData import *
from datetime import datetime
sysid = '58_1'
rep = Reports.objects.get(sysid__exact=sysid)
report = ReportSerializer(rep)
data = report.data
print(json.dumps(data, indent=4))
exit()

# organize data
pub = data['pub']
dst = data['set']
ref = dst[0]['reference']
subs = []
chemicals = data['chem']
chems = []

# this is a for loop
# the data pulled here "only" exists w/in the loop
for chemical in chemicals:
    subs.append(dict(chemical['sub']))
    chem = {}

    # info that will have stuff in it
    chem.update({'name': chemical['name']})
    chem.update({'description': chemical['description']})
    chem.update({'compnum': chemical['compnum']})

    # may or may not have info in it
    if chemical['comments'] is not None:
        chem.update({'comments': chemical['comments']})

    chems.append(chem)
# chemsubtances


# compound info is the "sub" info,general info about the chems

# create json-ld file
test = SciData(sysid)
test.context(['https://stuchalk.github.io/scidata/contexts/sds.jsonld',
              'https://stuchalk.github.io/scidata/contexts/scidata.jsonld'])
test.add_namespace({'w3i': 'https://w3id.org/skgo/modsci#'})
test.add_base("https://scidata.unf.edu/iupac/sds/" + sysid + "/")
test.version('1')
test.generatedat(str(datetime.now()))

# add general metadata
test.title('Solubility data from volume ' + pub['volume'])
austr = data['set'][0]['reference']['authors']
aulist = austr.split("; ")
aus = []
for au in aulist:
    aus.append({'name': au})
test.author(aus)


test.publisher('The International Union of Pure and Applied Chemistry')
test.add_keyword('Solubility')
test.add_keyword('Solubility data series')
test.discipline('w3i:Chemistry')
test.subdiscipline('w3i:PhysicalChemistry')
test.description('Critically reviewed solubility data reported in the IUPAC Solubility Data Series')

# SciData section

# methodology

# add the method info as an aspect under methodology of type procedure
# test.aspects

# system
chms = []
fields = ['name', 'description', 'compnum']
for chem in chems:
    chm = {"@id": "chemical", "@type": "sdo:chemical"}
    for field in fields:
        chm.update({field: chem[field]})
    chms.append(chm)
test.facets(chms)

subzs = []
fields = ['name', 'id', 'casno', 'formula']
for sub in subs:
    subz = {"@id": "compound", "@type": "sdo:compound"}
    for field in fields:
        subz.update({field: sub[field]})
    subzs.append(subz)
test.facets(subzs)

# add the chemical system

# dataset

# sources
test.add_source([{"title": pub['title'], "year": pub['year'], "type": "Critically evaluate report"}])
if ref:
    test.add_source([{"title": ref['title'], "year": ref['year'], "type": "Journal article", "doi": ref['doi']}])

# rights
test.rights("https://creativecommons.org/licenses/by-nc/4.0/", "NIST & IUPAC")

# generate JSON-LD
output = test.output

print(json.dumps(output, indent=4))
