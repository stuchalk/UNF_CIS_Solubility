from django.shortcuts import render
from sds.serializers import *
from .forms import *
from django.utils import timezone
from django.shortcuts import redirect


def add_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('view')
    else:
        form = ReportForm()
    return render(request, 'reports/reports_new.html', {'form': form})

def index():
    """ this is a test """
    print("Hellow world")


def view(request, repid=0):
    """ show data about a specific report """
    rep = Reports.objects.get(id=repid)
    report = ReportSerializer(rep)
    data = report.data
    sys = data['system']
    vol = data['volume']
    sysid = sys['id']
    # get from subsys table as not in serializer output
    subsyslst = SubstancesSystems.objects.all().filter(system_id=sysid).values('substance_id', 'compnum', 'role')
    compnts = {}
    for subsys in subsyslst:
        compnts.update({subsys['substance_id']: {'compnum': subsys['compnum'], 'role': subsys['role']}})
    method = data['method']
    variables = data['variables']
    chems = data['chem']
    series = data['set'][0]['dataseries']
    points = data['set'][0]['datapoints']
    subs = {}
    for chem in chems:
        subs.update({chem['compnum']: chem['substance']})
    refs = data['refs']
    mrefs = []
    for ref in refs:
        if ref['type'] == 'supplemental':
            mrefs.append(ref);

    cmplrs = data['authrep']
    return render(request, "../templates/reports/view.html",
                  {'sys': sys, 'vol': vol, 'subs': subs, 'vars': variables, 'series': series, 'points': points,
                   'method': method, 'chems': chems, 'refs': refs, 'mrefs': mrefs, 'cmplrs': cmplrs})
