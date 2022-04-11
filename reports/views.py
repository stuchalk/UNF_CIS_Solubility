from django.shortcuts import render
from sds.serializers import *
from .forms import *
from django.utils import timezone
from django.shortcuts import redirect


def add(request):
    if request.method == "POST":
        form_refs = ReferencesForm(request.POST, prefix='ref')
        form_reports = ReportsForm(request.POST, prefix='reports')
        form_conds = ConditionsForm(request.POST, prefix='conditions')
        form_data = DataForm(request.POST, prefix='data')
        if form_data.is_valid() and form_conds.is_valid() and form_reports.is_valid():
            # save report data
            post_rpt = form_reports.save(commit=False)
            post_rpt.save()
            # save dataset
            dataset = Datasets()
            vol = post_rpt.volume
            page = post_rpt.page
            dataset.title = "Dataset for " + str(vol) + ", page " + page
            dataset.description = "One datapoint"
            dataset.report_id = post_rpt.id
            dataset.comments = "via report add page"
            dataset.save()
            # save datapoint
            point = Datapoints()
            point.title = str(vol) + ", page " + page
            point.dataset_id = dataset.id
            point.rownum = 1
            point.save()
            # save condition
            post_conds = form_conds.save(commit=False)
            post_conds.datapoint_id = point.id
            post_conds.save()
            post_data = form_data.save(commit=False)
            post_data.datapoint_id = point.id
            post_data.save()
            return redirect('view/' + str(post_rpt.id))
        else:
            print('Form input error...')
    else:
        form_refs = ReferencesForm(prefix='ref')
        form_reports = ReportsForm(prefix='reports')
        form_conds = ConditionsForm(prefix='conditions')
        form_data = DataForm(prefix='data')
    return render(request, 'reports/add.html',
                  {'form_conds': form_conds, 'form_data': form_data,
                   'form_reports': form_reports, 'form_refs': form_refs})


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
            mrefs.append(ref)

    cmplrs = data['authrep']
    return render(request, "../templates/reports/view.html",
                  {'sys': sys, 'vol': vol, 'subs': subs, 'vars': variables, 'series': series, 'points': points,
                   'method': method, 'chems': chems, 'refs': refs, 'mrefs': mrefs, 'cmplrs': cmplrs})
