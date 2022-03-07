""" urls for the substances app """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='substance index'),
    path("view/<subid>", views.view, name='substance view'),

]
