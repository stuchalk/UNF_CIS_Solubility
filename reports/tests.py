""" django unit test file"""
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()
from reports.serializers import *
from scidatalib.scidata import *
from datetime import datetime
sysid = '58_1'
rep = Reports.objects.get(sysid__exact=sysid)
report = ReportSerializer(rep)
data = report.data

# organize data
pub = data['pub']
dst = data['set'][0]
ref = dst['reference']
subs = []
chemicals = data['chem']
chems = []
csysts = []
sys = dst['system']

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
test.namespaces({'w3i': 'https://w3id.org/skgo/modsci#'})
test.base("https://scidata.unf.edu/iupac/sds/" + sysid + "/")
test.version('1')

# additional namespaces
test.namespaces({
    "sdo": "https://stuchalk.github.io/scidata/ontology/scidata.owl#",
    "dc": "http://purl.org/dc/terms/",
    "qudt": "http://qudt.org/vocab/unit/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "gb": "https://goldbook.iupac.org/",
    "so": "https://stuchalk.github.io/scidata/ontology/solubility.owl#",
    "ss": "http://semanticscience.org/resource/",
    "obo": "http://purl.obolibrary.org/obo/",
    "afrl": "http://purl.allotrope.org/ontologies/role#"})

# add general metadata
test.title('Solubility data from volume ' + pub['volume'])
austr = data['set'][0]['reference']['authors']
aulist = austr.split("; ")
aus = []
for au in aulist:
    aus.append({'name': au})
test.author(aus)

test.publisher('The International Union of Pure and Applied Chemistry')
test.keywords('Solubility')
test.keywords('Solubility data series')
test.discipline('w3i:Chemistry')
test.subdiscipline('w3i:PhysicalChemistry')
test.description('Critically reviewed solubility data reported in the IUPAC Solubility Data Series')

# SciData section

# methodology
# test.aspects(data['method'])
# add the method info as an aspect under methodology of type procedure

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
# iterate over idents to get iupac and inchi
idents = ['iupacname', 'inchikey']
subsys = sys['subsys']
for ss in subsys:
    sub = ss['substance']
    idees = sub['identifier']
    subz = {"@id": "compound", "@type": "sdo:compound"}
    for field in fields:
       subz.update({field: sub[field]})
    for ident in idents:
        for idee in idees:
            if idee["type"] == ident:
                subz.update({ident: idee['value']})
    subzs.append(subz)
print(json.dumps(subzs, indent=4))
exit()
test.facets(subzs)

chemsystems = []
fields = ['name','type','constituents']
# system or chemical system
chemsystem = {"@id": "chemicalsystem", "@type": "sdo:chemicalsystem"}
chemsystem.update({'name': sys['name']})
print(chemsystem)
exit()
for field in fields:
    chemsystem.update({field: chemsystem[field]})
    for constituent in chemsystem:
        pass

chemsystems.append(chemsystem)
test.facets(chemsystems)

# dataset

# sources
test.sources([{"title": pub['title'], "year": pub['year'], "type": "Critically evaluate report"}])
if ref:
    test.sources([{"title": ref['title'], "year": ref['year'], "type": "Journal article", "doi": ref['doi']}])

# rights
test.rights("https://creativecommons.org/licenses/by-nc/4.0/", "NIST & IUPAC")

# generate JSON-LD
output = test.output

print(json.dumps(output, indent=4))
