""" substance views file """
from django.shortcuts import render
from sds.models import *


def index(request):
    """ present an overview page about the substance in the sds"""
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
