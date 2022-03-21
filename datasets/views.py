""" dataset views file"""
from django.shortcuts import render
from sds.models import *


def index(request):
    """ present an overview page about the substance in the sds"""
    subcount = Substances.objects.count()
    idcount = Identifiers.objects.count()
    syscount = Systems.objects.count()

    return render(request, "../templates/datasets/index.html",
                  {'subcount': subcount, 'idcount': idcount, 'syscount': syscount})
