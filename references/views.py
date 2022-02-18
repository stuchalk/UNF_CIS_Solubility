""" substance views file """
from django.shortcuts import render
from sds.models import *


def index(request):
    """ present an overview page about the substance in the sds"""
    refs = References.objects.all().values('id', 'citation')
    return render(request, "../templates/references/index.html", {'refs': refs})
