""" substance views file """
import urllib.error
import urllib.request
from django.shortcuts import render
from sds.models import *


def index(request):
    """
    present an overview page about the substance in the sds"""
    data = Substances.objects.all().values('id', 'name').order_by('name')
    chars = []
    subs = {}
    for s in data:
        first = s['name'][0].upper()
        if first not in subs.keys():
            subs.update({first: []})
            chars.append(first)
        subs[first].append(tuple((s['id'], s['name'])))
    return render(request, "../templates/substances/index.html", {'subs': subs, 'chars': chars})


def view(request, subid=0):
    """ show data about a specific substance"""
    sub = Substances.objects.get(id=subid)
    # get identifiers
    idents = sub.identifiers_set.values('type', 'value')
    ids = {}
    for iid in idents:
        if iid['type'] not in ids.keys():
            ids[iid['type']] = iid['value']
        else:
            ids[iid['type']] += ", " + iid['value']
    # systems that this substance is a component in
    sysids = sub.substancessystems_set.values_list('system_id')
    syslst = Systems.objects.all().filter(id__in=sysids).values('id', 'name').order_by('name')
    # get compilation report(s)
    crpts = Datasets.objects.all().filter(system__in=sysids, eval=0).values('report_id', 'system_id',
                                                                            'report__referencesreports__reference__raw')
    # get compilation report
    erpts = Datasets.objects.all().filter(system__in=sysids, eval=1).values('report_id', 'system_id')
    # agregate data for template
    syss = {}
    for sys in syslst:
        if sys['id'] not in syss.keys():
            syss.update({sys['id']: []})
        syss[sys['id']].append(sys['name'])
        elst = []
        for erpt in erpts:
            if erpt['system_id'] == sys['id']:
                elst.append(erpt['report_id'])
        syss[sys['id']].append(elst)
        clst = []
        for crpt in crpts:
            if crpt['system_id'] == sys['id']:
                clst.append(tuple((crpt['report_id'], crpt['report__referencesreports__reference__raw'])))
        syss[sys['id']].append(clst)

    # work out if pubchem has 3d version of sdf file
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/' + ids['inchikey'] + '/SDF?record_type=3d'
    dim = 3
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        dim = 2

    # send data to template
    return render(request, "../templates/substances/view.html",
                  {'sub': sub, 'ids': ids, 'syss': syss, 'dim': dim})
