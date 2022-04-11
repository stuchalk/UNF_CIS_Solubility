from django import forms
from sds.models import *

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        exclude = ['updated', 'datapoint']

class DatapointsForm(forms.ModelForm):
    class Meta:
        model = Datapoints
        exclude = ['updated']


# class QuantitiesForm(forms.ModelForm):
#     class Meta:
#         model = Quantities
#         exclude = ['updated']

#
# class UnitsForm(forms.ModelForm):
#     class Meta:
#         model = Units
#         exclude = ['updated']


