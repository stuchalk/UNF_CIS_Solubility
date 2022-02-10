""" django unit test file"""
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from reports.serializers import *
from scidatalib.scidata import *
import json

sysid = '58_1'
rep = Reports.objects.get(sysid__exact=sysid)
report = ReportSerializer(rep)
data = report.data
f = open(sysid + ".json", "w")
f.write(json.dumps(data))
print(json.dumps(data, indent=4))
exit()

# organize data
pub = data['pub']
dst = data['set'][0]
ref = dst['reference']
subs = []
chemicals = data['chem']
chems = []
csysts = []
sys = dst['system']
points = dst['dataseries'][0]['datapoints']
conditions = []
# cond_properties = []
# cond_properties_baseunit = []
# cond_units = []
data_points = []

# get chemicals (substance instance) data and populate subs variable
for chemical in chemicals:
    subs.append(dict(chemical['substance']))
    chem = {}

    # info that will have stuff in it
    chem.update({'name': chemical['name']})
    chem.update({'description': chemical['description']})
    chem.update({'compnum': chemical['compnum']})

    # may or may not have info in it
    if chemical['comments'] is not None:
        chem.update({'comments': chemical['comments']})

    chems.append(chem)

# get conditions and related condition properties/units
for point in points:
    conditions.append(point['conditions'])
# for condition in conditions:
#     cond_properties.append(condition[0]['property'])
#     cond_units.append(condition[0]['unit'])
# for property in cond_properties:
#     cond_properties_baseunit.append(property['baseunit'])

# get data values
for point in points:
    data_points.append(point['data'])

# create json-ld file
test = SciData(sysid)
test.context(['https://stuchalk.github.io/scidata/contexts/sds.jsonld',
              'https://stuchalk.github.io/scidata/contexts/scidata.jsonld'])
test.namespaces({'w3i': 'https://w3id.org/skgo/modsci#'})
test.base("https://scidata.unf.edu/iupac/sds/" + sysid + "/")
test.version('1')

# add additional namespaces
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
test.description('Critically reviewed solubility data reported '
                 'in the IUPAC Solubility Data Series')

# SciData section

# methodology
# add the method info (data['method']) as procedure
proc = [{"@id": "procedure", "description": data['method']}]
test.aspects(proc)

# system
# add substances
subs = []
fields = ['name', 'id', 'casno', 'formula']
# iterate over idents to get iupac and inchi
idents = ['iupacname', 'inchikey']
subsyss = sys['subsys']
for subsys in subsyss:
    subb = subsys['substance']
    idees = subb['identifier']
    sub = {"@id": "compound", "@type": "sdo:compound"}
    for field in fields:
        sub.update({field: subb[field]})
    for ident in idents:
        for idee in idees:
            if idee["type"] == ident:
                sub.update({ident: idee['value']})
    del sub['id']
    subs.append(sub)
test.facets(subs)

# add constituents
constituents = []
for chem in chems:
    constituent = {"@id": "constituent", "@type": "sdo:constituent"}
    constituent.update({'compound': 'compound ' + str(chem['compnum'])})
    constituent.update({'role': 'placeholder'})
    constituents.append(constituent)

# add chemicalsystems
chemsystems = []
systype = {"1": "pure compound", "2": "binary system", "3": "ternary system", "4": "quaternary system"}
# system or chemical system
chemsystem = {"@id": "chemicalsystem", "@type": "sdo:chemicalsystem"}
chemsystem.update({'name': sys['name']})
chemsystem.update({'type': systype[str(sys['components'])]})
chemsystem.update({'constituents': constituents})
chemsystems.append(chemsystem)
test.facets(chemsystems)

# add chemicals
chms = []
fields = ['name', 'description', 'compnum']
for chem in chems:
    chm = {"@id": "chemical", "@type": "sdo:chemical"}
    for field in fields:
        chm.update({field: chem[field]})
    chms.append(chm)
test.facets(chms)

# add value array for conditions
valuearray = []
for condition in conditions:
    value = {"@id": "value", "@type": "sdo:numericValue"}
    value.update({'datatype': 'float'})
    # 'sigfigs' has been hard-coded to remove the decimal point from the significand
    # if there is no decimal point in the significand the 'sigfigs' may be wrong
    value.update({'sigfigs': len(str(condition[0]['significand']).replace('.', ''))})
    value.update({'number': condition[0]['significand']})
    value.update({'unit': condition[0]['unit']['symbol']})
    value.update({'error': condition[0]['error']})
    value.update({'errornote': 'placeholder'})
    valuearray.append(value)

# define name/number of conditions
condish = []
for condition in conditions:
    name = condition[0]['property']['name']
    if name not in condish:
        condish.append(name)

# add conditions
conds = []
for condi in condish:
    cond = {"@id": "condition", "@type": "sdo:condition"}
    cond.update({'property': condi})
    cond.update({'propertyref': 'placeholder'})
    cond.update({'valuearray': valuearray})
    conds.append(cond)
test.facets(conds)

# dataset
# datagroup
datagroup = []
series = dst['dataseries']
title = ref['title']
d_points = []
for thing in data_points:
    d_points.append('datapoint')
for serie in series:
    dataserie = {"@id": "dataseries", "@type": "sdo:dataseries"}
    dataserie.update({'title': title})
    dataserie.update({'system': chemsystem["@id"]})
    dataserie.update({'datapoints': d_points})
    datagroup.append(dataserie)
test.datagroup(datagroup)


# add data
datums = []
for data_p in data_points:
    datum = {"@id": "datum", "@type": "sdo:exptdata"}
    datum.update({'property': data_p[0]['property']['name']})
    datum.update({'propertyref': 'placeholder'})
    datum.update({'numericvalue': 'placeholder'})
    datums.append(datum)

# add datapoints
datapoints = []
fields = ['uid', 'conditions', 'data']
x = 0
for point in points:
    datapoint = {"@id": "datapoint", "@type": "sdo:datapoint"}
    datapoint.update({'uid': point['sysid_tablenum_rownum']})
    datapoint.update({'conditions': valuearray[x]['@id']})
    x += 1
    datapoint.update({'data': datums})
    datapoints.append(datapoint)
    if x > len(valuearray):
        break
test.datapoint(datapoints)

# sources
test.sources([{"title": pub['title'], "year": pub['year'],
               "type": "Critically evaluate report"}])
if ref:
    test.sources([{"title": ref['title'], "year": ref['year'],
                   "type": "Journal article", "doi": ref['doi']}])

# rights
test.rights("https://creativecommons.org/licenses/by-nc/4.0/", "NIST & IUPAC")

# generate JSON-LD
output = test.output
print(json.dumps(output, indent=4))
