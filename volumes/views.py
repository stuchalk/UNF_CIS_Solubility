""" substance views file """
from django.shortcuts import render, redirect
from sds.models import *


def index(request, display='volumes'):
    """ present an overview page about the substance in the sds"""
    if display == 'volumes':
        vols = Publications.objects.all().values('volume', 'title')
    else:
        vols = Publications.objects.all().values('id', 'title')
    return render(request, "../templates/volumes/index.html", {'vols': vols, "display": display})


def view(request, volume=''):
    """ get the data about a volume """
    if volume == '':
        response = redirect('/')
        return response
    else:
        if volume[0] == 'v':
            vol = Publications.objects.get(volume=volume[1:])
        else:
            vol = Publications.objects.get(id=volume)
    sets = Datasets.objects.filter(sysid__contains=str(vol.id) + '_').\
        select_related('system').all().order_by('system__name')
    syss = {}
    chars = []
    for s in sets:
        first = s.system.name[0].upper()
        if first not in syss.keys():
            syss.update({first: []})
            chars.append(first)
        syss[first].append(tuple((s.report_id, s.system.name)))
    return render(request, "../templates/volumes/view.html", {'vol': vol, 'syss': syss, 'chars': chars})
