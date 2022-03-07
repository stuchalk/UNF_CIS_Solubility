from django.shortcuts import render
from django.db.models.functions import *
from sds.models import *
from sds.functions import *


def index(request):
    """ present an overview page about the substance in the sds"""
    data = Systems.objects.all().values('id', 'name').order_by('name').annotate(first=Upper(Substr('name', 1, 1)))
    lst = list(data)
    syss = groupbyfirst(lst)
    chars = syss.keys()

    return render(request, "../templates/systems/index.html", {'syss': syss})
