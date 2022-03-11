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


def view(request, refid=0):
    """ show data about a specific reference"""
    ref = References.objects.get(id=refid)
    rprtids = ReferencesReports.objects.all().filter(reference_id=refid).values_list('report_id', flat=True)
    rdsets = Datasets.objects.all().filter(report_id__in=rprtids).values('report_id', 'system__name')
    evalids = EvaluationsReferences.objects.all().filter(reference_id=refid).values_list('evaluation_id', flat=True)
    erptids = Evaluations.objects.all().filter(id__in=evalids).values_list('report_id', flat=True)
    edsets = Datasets.objects.all().filter(id__in=erptids).values('report_id', 'system__name')

    return render(request, "../templates/references/view.html", {'ref': ref, 'evals': edsets, 'dsets': rdsets})
