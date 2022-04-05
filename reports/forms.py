from django import forms
from sds.models import *

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ('id', 'volume', 'page', 'system', 'type', 'variables', 'method', 'comments')



