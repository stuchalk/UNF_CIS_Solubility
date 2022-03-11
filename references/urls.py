""" urls for the references app """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("view/<refid>", views.view, name='reference view'),
]
