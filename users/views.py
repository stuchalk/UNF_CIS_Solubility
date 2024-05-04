from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from sds.models import *


def index(request):
    """present an overview page about the substance in the sds"""
    usrs = (User.objects.all().filter(last_login__gt='2024-03-01').
            values('id', 'first_name', 'last_name').order_by('last_name'))
    for usr in usrs:
        # stats on conditions, data, and suppdata fields
        cids = (LogEntry.objects.all().
                filter(user_id=usr['id'], content_type_id=16, action_flag=1).values_list('object_id', flat=True))
        dids = (LogEntry.objects.all().
                filter(user_id=usr['id'], content_type_id=17, action_flag=1).values_list('object_id', flat=True))
        sids = (LogEntry.objects.all()
                .filter(user_id=usr['id'], content_type_id=33, action_flag=1).values_list('object_id', flat=True))
        ccnt = cids.count()
        dcnt = dids.count()
        scnt = sids.count()
        usr.update({'concnt': ccnt})
        usr.update({'datcnt': dcnt})
        usr.update({'supcnt': scnt})
        usr.update({'total': ccnt + dcnt + scnt})
        # grading data: conditions, data, suppdata entries with errors in comments fields
        cons = Conditions.objects.all().filter(id__in=cids, comments__isnull=False).count()
        data = Data.objects.all().filter(id__in=dids, comments__isnull=False).count()
        supp = Suppdata.objects.all().filter(id__in=sids, comments__isnull=False).count()
        if cons > 0:
            usr.update({'conerr': round((cons*100)/ccnt, 1)})
        else:
            usr.update({'conerr': 0})
        if data > 0:
            usr.update({'daterr': round((data*100)/dcnt, 1)})
        else:
            usr.update({'daterr': 0})
        if supp > 0:
            usr.update({'superr': round((supp*100)/scnt, 1)})
        else:
            usr.update({'superr': 0})
    return render(request, "../templates/users/index.html", {'usrs': usrs})


def view(request, usrid=0):
    """ show data about a specific substance"""
    usr = User.objects.get(id=usrid)
    # content_type = 26 are reports, list includes deleted reports
    rptids = list(LogEntry.objects.filter(user=usr, content_type_id=26, action_flag=1).values_list('object_id', flat=True))
    rptlst = Reports.objects.filter(id__in=rptids)  # ignores deleted reports
    rpts = {}
    for rpt in rptlst:
        title = rpt.volume.vol + ": " + rpt.system.name
        rpts.update({rpt.id: title})
    return render(request, "../templates/users/view.html", {'usr': usr, 'rpts': rpts})
