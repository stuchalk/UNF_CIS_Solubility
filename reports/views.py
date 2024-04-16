""" django view file for reports """
from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.http import JsonResponse
from scidatalib.scidata import *


def add(request):
    """ method to add a report """
    if request.method == "POST":
        form_refs = ReferencesReportsForm(request.POST, prefix='ref')
        form_reports = ReportsForm(request.POST, prefix='reports')
        form_conds = ConditionsForm(request.POST, prefix='conditions')
        form_data = DataForm(request.POST, prefix='data')
        if form_data.is_valid() and form_conds.is_valid() and form_reports.is_valid():
            # save report data
            post_rpt = form_reports.save(commit=False)
            post_rpt.save()
            # save orginal ref
            oriref = ReferencesReports()
            oriref.reference_id = form_refs.reference.id
            oriref.report_id = post_rpt.id
            oriref.type = 'original'
            oriref.methodrefnum = 0
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
        form_refs = ReferencesReportsForm(prefix='ref')
        form_reports = ReportsForm(prefix='reports')
        form_conds = ConditionsForm(prefix='conditions')
        form_data = DataForm(prefix='data')
    return render(request, 'reports/add.html',
                  {'form_conds': form_conds, 'form_data': form_data,
                   'form_reports': form_reports, 'form_refs': form_refs})


def index():
    """ display an index of reports (needed?) """
    pass


def view(request, repid=0):
    """ show data about a specific report """
    rep = Reports.objects.get(id=repid)
    sys = rep.system
    vol = rep.volume
    sysid = sys.id
    subsyslst = SubstancesSystems.objects.all().filter(system_id=sysid).values('substance_id', 'compnum', 'role')
    compnts = {}
    for subsys in subsyslst:
        compnts.update({subsys['substance_id']: {'compnum': subsys['compnum'], 'role': subsys['role']}})
    method = rep.method
    variables = rep.variables
    chems = rep.chemicals_set.all()
    subs = {}
    for chem in chems:
        subs.update({chem.compnum: chem.substance})
    sets = rep.datasets_set.all()
    # TODO: Get user usr = User.objects.get(username=rep.username)
    if sets.count() > 0:
        series = sets[0].dataseries_set.all()
        orefids = rep.referencesreports_set.all().filter(type='original').values_list('reference_id', flat=True)
        mrefids = rep.referencesreports_set.all().filter(type='supplemental').values_list('reference_id', flat=True)
        orefs = References.objects.filter(id__in=orefids)
        mrefs = References.objects.filter(id__in=mrefids)
        cmplrs = rep.authorsreports_set.all().filter(role='compiler')
        return render(request, "../templates/reports/view.html",
                  {'sys': sys, 'vol': vol, 'subs': subs, 'vars': variables, 'series': series, 'method': method,
                   'chems': chems, 'orefs': orefs, 'mrefs': mrefs, 'cmplrs': cmplrs, 'compnts': compnts})
    else:
        return render(request, "../templates/reports/nodata.html")


def scidata(request, repid=0):
    """ output report as scidata.jsonld"""
    rep = Reports.objects.get(id=repid)
    vol = rep.volume
    sets = rep.datasets_set.all()
    chems = rep.chemicals_set.all()
    orefids = rep.referencesreports_set.all().filter(type='original').values_list('reference_id', flat=True)
    mrefids = rep.referencesreports_set.all().filter(type='supplemental').values_list('reference_id', flat=True)
    orefs = References.objects.filter(id__in=orefids)
    mrefs = References.objects.filter(id__in=mrefids)
    cmplrs = rep.authorsreports_set.all().filter(role='compiler')
    sys = rep.system
    sysid = sys.id
    subsyss = SubstancesSystems.objects.all().filter(system_id=sysid)
    subids = SubstancesSystems.objects.all().filter(system_id=sysid).values_list('substance_id', flat=True)
    subts = Substances.objects.filter(id__in=subids)

    # organize data
    chms = []
    subs = []
    conds = []
    sconds = []
    datums = []
    sdatas = []

    # create json-ld file
    test = SciData(sysid)
    test.context(['https://stuchalk.github.io/scidata/contexts/sds.jsonld',
                  'https://stuchalk.github.io/scidata/contexts/scidata.jsonld'])
    test.namespaces({'w3i': 'https://w3id.org/skgo/modsci#'})
    test.base("https://scidata.unf.edu/iupac/sds/" + str(sysid) + "/")
    test.version('1')

    # add additional namespaces
    test.namespaces({
        "sdo": "https://stuchalk.github.io/scidata/ontology/scidata.owl#",
        "dc": "http://purl.org/dc/terms/",
        "qudt": "https://qudt.org/vocab/unit/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "gb": "https://goldbook.iupac.org/",
        "so": "https://stuchalk.github.io/scidata/ontology/solubility.owl#",
        "ss": "https://semanticscience.org/resource/",
        "obo": "http://purl.obolibrary.org/obo/",
        "afrl": "http://purl.allotrope.org/ontologies/role#"})

    # add general metadata
    test.title('Solubility data from volume ' + vol.volume)
    aus = []
    for aureps in cmplrs:
        aus.append({'name': aureps.author.name})
    test.author(aus)
    test.publisher('The International Union of Pure and Applied Chemistry')
    test.keywords('Solubility')
    test.keywords('Solubility data series')
    test.discipline('w3i:Chemistry')
    test.subdiscipline('w3i:PhysicalChemistry')
    test.description('Critically reviewed solubility data reported '
                     'in the IUPAC Solubility Data Series')

    # SciData section

    # methodology
    # add the method info (data['method']) as procedure
    proc = [{"@id": "procedure", "description": rep.method}]
    test.aspects(proc)

    # system
    # get chemicals (substance instance) data and populate subs variable
    for chem in chems:
        chm = {}
        # info that will have stuff in it
        chm.update({'@id': 'chemical'})
        chm.update({'name': chem.substance.name})
        chm.update({'supplier': chem.supplier})
        chm.update({'substance': 'substance/' + str(chem.compnum) + '/'})
        # add to list
        chms.append(chm)

    # get substances data
    for subt in subts:
        sub = {}
        # info that will have stuff in it
        sub.update({'@id': 'substance'})
        sub.update({'name': subt.name})
        sub.update({'formula': subt.formula})
        sub.update({'molweight': subt.molweight})
        for ident in subt.identifiers_set.all():
            sub.update({ident.type: ident.value})
        subs.append(sub)

    # add mixture data
    mix = {'@id': 'mixture'}
    mix.update({'name': sys.name})
    mix.update({'components': sys.components})
    constituents = []
    for subsys in subsyss:
        constituent = {"@id": "constituent"}
        constituent.update({'substance': 'substance ' + str(subsys.compnum)})
        constituent.update({'substance#': 'substance/' + str(subsys.compnum) + '/'})
        constituent.update({'constituent': subsys.compnum})
        constituent.update({'role': subsys.role})
        constituents.append(constituent)
    mix.update({'constituents': constituents})

    test.facets(subs)
    test.facets([mix])
    test.facets(chms)

    # dataseries
    dset = sets[0]
    for ser in dset.dataseries_set.all():
        scnds = ser.conditions_set.all().values()
        for scnd in scnds:
            quant = Quantities.objects.get(id=scnd['quantity_id'])
            scnd['quantity'] = quant.name
            sconds.append(scnd)
        for point in ser.datapoints_set.all():
            cnds = point.conditions_set.all().values()
            for cnd in cnds:
                conds.append(cnd)
            datms = point.data_set.all().values()
            for datm in datms:
                datums.append(datm)
            supps = point.suppdata_set.all().values()
            for supp in supps:
                sdatas.append(supp)

    # add value array for conditions
    condarray = []
    for cond in conds:
        value = {"@id": "value", "@type": "sdo:numericValue"}
        value.update({'datatype': 'float'})
        value.update({'sigfigs': cond['accuracy']})
        value.update({'number': cond['text']})
        value.update({'unit': cond['symbol']})
        condarray.append(value)

    # define name/number of conditions
    uconds = []
    for cond in conds:
        name = cond[0]['quantity']['name']
        if name not in uconds:
            uconds.append(name)

    # add conditions
    conds = []
    for ucond in uconds:
        cond = {"@id": "condition", "@type": "sdo:condition"}
        cond.update({'quantity': ucond.name})
        cond.update({'quantity#': 'add crosswalk'})
        cond.update({'valuearray': condarray})
        conds.append(cond)
    test.facets(conds)

    # add series conditions
    # define name/number of series conditions
    usconds = []
    for scond in sconds:
        name = scond.quantity.name
        if name not in usconds:
            usconds.append(name)

    return JsonResponse(usconds, status=200, safe=False)

    # dataset
    # datagroup
    # x = 0
    # datagroup = []
    # allseries = dst['dataseries']
    # for series in allseries:
    #     group = {"@id": "datagroup", "@type": "sdo:datagroup"}
    #     group.update({'title': 'Datagroup ' + str(x + 1)})
    #     group.update({'system': chemsystem["@id"]})
    #     dpoints = []
    #     for point in series['datapoints']:
    #         dpoint = {"@id": "datapoint", "@type": "sdo:datapoint"}
    #         dpoint.update({'uid': point['sysid_tablenum_rownum']})
    #         dpoint.update({'conditions': [condarray[x]['@id']]})
    #         datums = []
    #         for datum in point['data']:
    #             d = {"@id": "datum", "@type": "sdo:exptdata"}
    #             d.update({'property': datum['property']['name']})
    #             d.update({'property#': 'add crosswalk'})
    #             nvalue = {"@id": "value", "@type": "sdo:numericvalue"}
    #             nvalue.update({'datatype': "xsd:float"})
    #             nvalue.update({'number': float(datum['significand']) * 10 ** int(datum['exponent'])})
    #             nvalue.update({'sigfigs': len(datum['significand']) - 1})
    #             d.update({'numericvalue': nvalue})
    #             datums.append(d)
    #         dpoint.update({"data": datums})
    #         dpoints.append(dpoint)
    #     group.update({'datapoints': dpoints})
    #     datagroup.append(group)
    #
    # print(json.dumps(datagroup, indent=4))
    # exit()
    # test.datagroup(datagroup)
    #

    # sources
    for ref in orefs:
        test.sources([{"@id": "source", "title": ref.title,
                       "year": str(ref.year), "type": "Primary source article", "doi": ref.doi}])

    for ref in mrefs:
        test.sources([{"@id": "source", "title": ref.title, "year": str(ref.year),
                       "type": "Method reference article", "doi": ref.doi}])

    # rights
    test.rights([{'license': "https://creativecommons.org/licenses/by-nc/4.0/", 'holder': "NIST & IUPAC"}])

    # generate JSON-LD
    output = test.output
    return JsonResponse(output, status=200)
