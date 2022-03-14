""" substance views file """
from django.shortcuts import render
from sds.models import *


def index(request):
    """
    present an overview page about the substance in the sds"""
    data = Substances.objects.all().values('id', 'name')
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
    for id in idents:
        if id['type'] not in ids.keys():
            ids[id['type']] = id['value']
        else:
            ids[id['type']] += ", " + id['value']
    # systems that this substance is a component in
    sysids = sub.substancessystems_set.values_list('system_id')
    syss = Systems.objects.all().filter(id__in=sysids).values_list('id', 'name').order_by('name')
    # get compilation report(s)
    crpts = Datasets.objects.all().filter(system__in=sysids, eval=0).values('report_id', 'system_id',
                                                                            'report__referencesreports__reference__raw')
    crptsbysys = {}
    for rpt in crpts:
        if rpt['system_id'] not in crptsbysys.keys():
            crptsbysys.update({rpt['system_id']: {}})
        crptsbysys[rpt['system_id']].update({rpt['report_id']: rpt['report__referencesreports__reference__raw']})
    # get evaluation report
    erpts = Datasets.objects.all().filter(system__in=sysids, eval=1).values('report_id', 'system_id')
    erptsbysys = {}
    for rpt in erpts:
        erptsbysys.update({rpt['system_id']: rpt['report_id']})
    return render(request, "../templates/substances/view.html",
                  {'sub': sub, 'ids': ids, 'syss': syss, 'crpts': crptsbysys, 'erpts': erptsbysys})
