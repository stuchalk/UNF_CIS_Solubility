""" view functions for the systems table """
import urllib.error
import urllib.request
from django.shortcuts import render
from sds.models import *


def index(request):
    """ present an overview page about the system in the sds """
    data = Systems.objects.all().values('id', 'name').order_by('name')
    chars = []
    syss = {}
    for s in data:
        first = s['name'][0].upper()
        if first not in syss.keys():
            syss.update({first: []})
            chars.append(first)
        syss[first].append(tuple((s['id'], s['name'])))
    return render(request, "../templates/systems/index.html", {'syss': syss, 'chars': chars})


def view(request, sysid=0):
    """ show data about a specific system """
    sys = Systems.objects.get(id=sysid)
    # substances that the system is part of
    subids = sys.substancessystems_set.values('substance_id').order_by('compnum')
    sublst = Substances.objects.all().filter(id__in=subids, identifiers__type='inchikey').\
        values_list('id', 'name', 'identifiers__value')
    subs = []  # this will hold the names and urls to get the sdf file for each substance
    pcpath = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/'
    for sub in sublst:
        url = pcpath + sub[2] + '/SDF?record_type=3d'
        try:
            urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            url = pcpath + sub[2] + '/SDF?record_type=2d'
        subs.append(tuple((sub[0], sub[1], url)))

    # eval that this system is analyzed in
    evals = Reports.objects.all().filter(system_id=sysid, type='evaluation').values('id')
    # reports this system
    rpts = Reports.objects.all().filter(system_id=sysid, type='compilation').\
        values('id', 'referencesreports__reference__citation')
    # send data to template
    return render(request, "../templates/systems/view.html",
                  {'sys': sys, 'subs': subs, 'evals': evals, 'rpts': rpts})
