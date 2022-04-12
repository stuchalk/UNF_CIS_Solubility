""" report form """
from django import forms
from sds.models import *


def get_refs():
    allrefs = [('', 'Select a reference')]
    reflist = References.objects.all().values_list('id', 'citation')
    for ref in reflist:
        allrefs.append(ref)
    return allrefs


def get_aus():
    allaus = [('', 'Select an author')]
    aulist = Authors.objects.all().values_list('id', 'name').order_by('name')
    for au in aulist:
        allaus.append(au)
    return allaus


class ReportsForm(forms.ModelForm):
    orireflist = forms.ChoiceField(
        choices=get_refs(),
        required=True,
        label='Original Measurement',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_ref-id'}),
    )
    methreflist = forms.ChoiceField(
        choices=get_refs(),
        required=True,
        label='Original Measurement',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_ref-methref'}),
    )
    aulist = forms.ChoiceField(
        choices=get_aus(),
        required=True,
        label='Prepared By',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_authors-first'}),
    )

    class Meta:
        model = Reports
        fields = ('id', 'volume', 'page', 'system', 'aulist', 'orireflist', 'methreflist', 'variables', 'method', 'comments')


class ReferencesReportsForm(forms.ModelForm):
    class Meta:
        model = ReferencesReports
        exclude = ['updated']


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Reports
        exclude = ['updated']


class ConditionsForm(forms.ModelForm):
    class Meta:
        model = Conditions
        exclude = ['updated', 'datapoint', 'dataseries']


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        exclude = ['updated', 'datapoint', 'dataseries']
