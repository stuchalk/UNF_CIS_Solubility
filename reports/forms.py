""" report form """
from django import forms
from sds.models import *


class ReportsForm(forms.ModelForm):
    class Meta:
        model = Reports
        # fields = ('id', 'volume', 'page', 'system', 'type', 'variables', 'method', 'comments')
        exclude = ['updated']


class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        exclude = ['updated']


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ('id', 'volume', 'page', 'system', 'type', 'variables', 'method', 'comments')


class ConditionsForm(forms.ModelForm):
    class Meta:
        model = Conditions
        exclude = ['updated', 'datapoint', 'dataseries']


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        exclude = ['updated', 'datapoint', 'dataseries']
