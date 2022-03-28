import urllib.error
import urllib.request
from django.shortcuts import render
from sds.models import *
from sds.serializers import *


def index():
    """ this is a test """
    print("Hellow world")


def view(request, repid=0):
    """ show data about a specific report """
    rep = Reports.objects.get(id=repid)
    report = ReportSerializer(rep)
    data = report.data
    sysid = data['sys']
    vol = data['vol']
    sys = data['set'][0]['sys']
    subs = []
    for temp in sys['subsys']:
        if temp['sysid'] == sysid:
            sub = temp['substance']
            for ident in sub['identifier']:
                sub.update({ident['type']: ident['value']})
            del sub['identifier']
            subs.append(sub)
    method = data['method']
    chems = data['chem']
    refs = data['refs']
    cmplrs = data['authrep']
    return render(request, "../templates/reports/view.html", {'sys': sys, 'vol': vol, 'subs': subs,
                                                              'method': method, 'chems': chems, 'refs': refs,
                                                              'cmplrs': cmplrs})


