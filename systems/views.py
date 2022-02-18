from django.shortcuts import render
from django.db.models.functions import *
from .models import *


def index(request):
    """ present an overview page about the substance in the sds"""
    syss = Systems.objects.annotate(Upper(Substr('name', 1, 1)))
    syss.objects.filter(id=1)

    return render(request, "../templates/systems/index.html", {'syss': syss})
