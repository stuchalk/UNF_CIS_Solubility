""" urls for the volumes app """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='volindex'),
    path("view/<volume>", views.view, name='volview'),
]
