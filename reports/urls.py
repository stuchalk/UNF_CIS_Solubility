""" urls for the systems app """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("view/<repid>", views.view, name='view'),
    path("add/", views.add, name='add'),
]
