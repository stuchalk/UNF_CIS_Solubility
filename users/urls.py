""" urls for the users app """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='user index'),
    path("view/<usrid>", views.view, name='user view'),
]
