""" substance views file """
from django.shortcuts import render
from sds.models import *


def index(request):
    """ present an overview page about the substance in the sds"""
    aus = Authors.objects.all().values('id', 'name')
    return render(request, "../templates/authors/index.html", {'aus': aus})
