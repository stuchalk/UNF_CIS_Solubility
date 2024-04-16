from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from sds.models import *


def index(request):
    """present an overview page about the substance in the sds"""
    usrs = (User.objects.all().filter(last_login__gt='2024-03-01').
            values('id', 'first_name', 'last_name').order_by('last_name'))
    return render(request, "../templates/users/index.html", {'usrs': usrs})


def view(request, usrid=0):
    """ show data about a specific substance"""
    usr = User.objects.get(id=usrid)
    rptids = LogEntry.objects.filter(user=usr, content_type_id=26).values_list('object_id', flat=True)
    rpts = {}
    for rptid in rptids:
        rpt = Reports.objects.get(id=rptid)
        title = rpt.volume.vol + ": " + rpt.system.name
        rpts.update({rptid: title})
    return render(request, "../templates/users/view.html", {'usr': usr, 'rpts': rpts})
