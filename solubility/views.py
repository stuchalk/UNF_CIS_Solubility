""" solubility views file """
from django.shortcuts import render
from sds.serializers import *
from .forms import *
from django.utils import timezone
from django.shortcuts import redirect


def index(request):
    """ front page of the website """
    return render(request, "solubility/index.html")

def add_data(request):
    if request.method == "POST":
        form_datapoints = DatapointsForm(request.POST, prefix='datapoints_')
        form_data = DataForm(request.POST, prefix='data_')
        if form_data.is_valid() and form_datapoints.is_valid():
        # if form_data.is_valid():

            post_datapoints = form_datapoints.save(commit=False)
            post_datapoints.published_date = timezone.now()
            post_datapoints.author = request.user
            post_datapoints.save()
            post_data = form_data.save(commit=False)
            post_data.published_date = timezone.now()
            post_data.author = request.user
            post_data.datapoint = post_datapoints
            post_data.save()
            return redirect('index')
    else:
        form_datapoints = DatapointsForm()
        form_data = DataForm()
    return render(request, 'solubility/add.html', {'form_datapoints': form_datapoints, 'form_data': form_data})
    # return render(request, 'solubility/add.html', {'form_data': form_data})