""" urls for the solubility app """
from django.urls import path
from . import views

# this is for the home page...
urlpatterns = [
    path("", views.index, name='index'),
]
