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
    ids = sub.identifiers_set.values_list('type', 'value')
    subids = sub.substancessystems_set.values_list('system_id')
    syss = Systems.objects.filter(id=subids)
    idlist = {}
    for idtype, value in ids:
        if idtype not in idlist.keys():
            idlist.update({idtype: []})
        idlist[idtype].append(value)
    print(idlist)
    return render(request, "../templates/substances/view.html", {'sub': sub, 'ids': idlist, 'syss': syss})
