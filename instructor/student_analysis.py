import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from rest_framework import serializers
from instructor.inspectdb import *
import json
from pathlib import Path
import glob


django_content_dict= {}
django_content = DjangoContentType.objects.values()
for x in django_content:
    django_content_dict.update({x['model']:x['id']})

def user_iterator(serializeddata, userid):
    for k,v in serializeddata.items():
        if type(v) is list:
            for vl in v:
                user_iterator({k: vl}, userid)
        elif type(v) is dict:
            contentuid = v.get('id', None)
            kunderscoreless = k.replace('_', '')
            contenttypeid = django_content_dict[kunderscoreless]
            adminloguserid = DjangoAdminLog.objects.filter(content_type_id = contenttypeid, object_id = contentuid).last()
            if adminloguserid:
                adminloguserid= adminloguserid.user_id
                authuser = AuthUser.objects.values('id', 'first_name', 'last_name').get(id = adminloguserid)
                v.update({'creator': str(authuser['id'])+'_'+authuser['first_name']+'_'+authuser['last_name']})
                for kk, vv in v.items():
                    user_iterator({kk:vv}, userid)
        else:
            pass
        return serializeddata

def student_analysis(studentdata):
    analysis = {}
    for dp in studentdata['datapoints']:
        dpid = dp['id']
        analysis.update({dpid:[]})
        num_condition = len(dp['conditions'])
        if num_condition == 0:
            analysis[dpid].append('No condition')
        for con in dp['conditions']:
            significand = con['significand']
            significanddig = significand.replace('.', '')
            lensignificand = len(significanddig)
            accuracy = con['accuracy']
            if lensignificand == accuracy:
                pass
            else:
                analysis[dpid].append('condition significand accuracy discrepancy')
        num_data = len(dp['data'])
        if num_data == 0:
            analysis[dpid].append('No data')
        for con in dp['data']:
            significand = con['significand']
            significanddig = significand.replace('.', '')
            lensignificand = len(significanddig)
            accuracy = con['accuracy']
            if lensignificand == accuracy:
                pass
            else:
                analysis[dpid].append('data significand accuracy discrepancy')
        if dp.get('datasets', None):
            if dp['datasets'].get('reports', None):
                if r'\u' in json.dumps(dp['datasets']['reports']['method']):
                    # analysis[dpid].append('encoding character in report method')
                    pass
                if dp['datasets']['reports'].get('references_reports', None):
                    for refrep in dp['datasets']['reports']['references_reports']:
                        if r'\u' in json.dumps(refrep['references']['citation']):
                            pass
                            # analysis[dpid].append('encoding character in reference citation')
                else:
                    analysis[dpid].append('no references_reports')
            else:
                analysis[dpid].append('no report')
        else:
            analysis[dpid].append('no dataset')
        if not analysis[dpid]:
            analysis.pop(dpid)

    dpwithprobs = len(analysis)
    dpwithoutprobs = len(studentdata['datapoints']) - dpwithprobs
    analysisquant = {
        'total datapoints': str(len(studentdata['datapoints'])),
        'datapoints without problems': str(dpwithoutprobs),
        'datapoints with problems': str(dpwithprobs)
    }
    analysis = {**analysisquant, **analysis}

    studentdata = {**{'analysis':analysis}, **studentdata}
    return studentdata


path = "/Users/n01448636/Documents/GoogleDrive/PycharmProjects/UNF_CIS_Solubility/instructor/dump/"
filenames = [os.path.basename(x) for x in glob.glob(path+'*.jsonld')]
# filenames = ['student_4_Mikal_Graves.jsonld'] # override

for filename in filenames:
    username = filename.replace('.', '_')
    username = username.split('_')
    username = username[1]+'_'+username[2]+'_'+username[3]
    with open(path+filename) as studentfile:
        studentdata = json.load(studentfile)
        userid = filename.split('_')[1]
        studentdata = user_iterator(studentdata, userid)
        studentdata = student_analysis(studentdata)

    base = Path('analysis')
    jsonpath = base / ('analysis_' + str(username) + '.jsonld')

    try:
        base.mkdir(parents=True, exist_ok=True)
        jsonpath.write_text(json.dumps(studentdata))
        # print(json.dumps(serialized_data))
        print("Completed: student_" + str(username))
    except:
        print('Invalid JSON-LD')
