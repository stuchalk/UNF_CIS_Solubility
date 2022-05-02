""" urls for the systems app """
from django.urls import path
from . import views


urlpatterns = [
    path("<user_id>", views.view, name='view'),
]
