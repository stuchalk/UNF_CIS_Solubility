""" references views file """
from django.shortcuts import render
from sds.models import *


def index(request):
    """ present an overview page about the references in the sds"""
    data = References.objects.all().values('id', 'raw')
    chars = []
    refs = {}
    for r in data:
        first = r['raw'][0].upper()
        if first not in refs.keys():
            refs.update({first: []})
            chars.append(first)
        refs[first].append(tuple((r['id'], r['raw'])))
    return render(request, "../templates/references/index.html", {'refs': refs, 'chars': chars})

def view(request, subid=0):
    """ show data about a specific reference"""
    ref = References.objects.get(id=subid)
    reps = Reports.objects.
    return render(request, "../templates/substances/view.html", {'sub': sub, 'ids': idlist, 'syss': syss})