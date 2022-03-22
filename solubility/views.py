""" solubility views file """
from django.shortcuts import render


def index(request):
    """ front page of the website """
    return render(request, "solubility/index.html")
