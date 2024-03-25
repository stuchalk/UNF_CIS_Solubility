""" references views file """
from django.shortcuts import render
from sds.models import *


def index(request):
    """ present an overview page about the references in the sds"""
    data = References.objects.all().values('id', 'citation')
    chars = []
    refs = {}
    for r in data:
        first = r['citation'][0].upper()
        if first not in refs.keys():
            refs.update({first: []})
            chars.append(first)
        refs[first].append(tuple((r['id'], r['citation'])))
    return render(request, "../templates/references/index.html", {'refs': refs, 'chars': chars})


def view(request, refid=0):
    """ show data about a specific reference"""
    ref = References.objects.get(id=refid)
    rrptids = ReferencesReports.objects.all().filter(reference_id=refid).values_list('report_id', flat=True)
    rdsets = Reports.objects.all().filter(id__in=rrptids, type='compilation').values('id', 'system__name')
    edsets = Reports.objects.all().filter(id__in=rrptids, type='evaluation').values('id', 'system__name')

    return render(request, "../templates/references/view.html", {'ref': ref, 'evals': edsets, 'dsets': rdsets})
