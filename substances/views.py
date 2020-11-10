""" substance views file """
from django.shortcuts import render
from .models import *


def index(request):
    """ present an overview page about the substance in the sds"""
    subcount = Substances.objects.count()
    idcount = Identifiers.objects.count()
    syscount = Systems.objects.count()

    return render(request, "substances/index.html", {'subcount': subcount, 'idcount': idcount, 'syscount': syscount})
