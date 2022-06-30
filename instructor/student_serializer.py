import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
django.setup()
from rest_framework import serializers
from instructor.inspectdb import *
import json
from pathlib import Path

class ReferencesReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferencesReports
        # fields = '__all__'
        exclude = ['reports']
        depth = 3

class SubstancesSystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubstancesSystems
        # fields = '__all__'
        exclude = ['systems']
        depth = 1

class SystemsSerializer(serializers.ModelSerializer):
    substances_systems = SubstancesSystemsSerializer(source='substancessystems_set', read_only=True, many=True)
    class Meta:
        model = Systems
        fields = '__all__'
        depth = 2

class ReportsSerializer(serializers.ModelSerializer):
    systems = SystemsSerializer()
    references_reports = ReferencesReportsSerializer(source='referencesreports_set', read_only=True, many=True)
    class Meta:
        model = Reports
        fields = '__all__'
        depth = 2

class DatasetsSerializer(serializers.ModelSerializer):
    reports = ReportsSerializer()
    class Meta:
        model = Datasets
        fields = '__all__'
        depth = 0

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields = '__all__'
        exclude = ['datapoints']
        depth = 1

class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        # fields = '__all__'
        exclude = ['datapoints']
        depth = 1


class DatapointsSerializer(serializers.ModelSerializer):
    conditions = ConditionsSerializer(source='conditions_set', read_only=True, many=True)
    data = DataSerializer(source='data_set', read_only=True, many=True)
    datasets = DatasetsSerializer()

    class Meta:
        model = Datapoints
        fields = '__all__'
        depth = 3

class DjangoAdminLogSerializer(serializers.ModelSerializer):
    # input_set_measured_properties = InputSetMeasuredPropertiesSerializer_build(source='inputsetmeasuredproperties_set', many=True, required=False)

    class Meta:
        model = DjangoAdminLog
        fields = '__all__'
        depth = 1


authusers = AuthUser.objects.values()
# authusers = [{'id': 4, 'username': 'n01423424', 'first_name': 'Mikal', 'last_name': 'Graves'}]

for auser in authusers:
    userid = auser['id']
    username = auser['first_name'] + '_' + auser['last_name']
    datapoints = []
    django_admin_object = DjangoAdminLog.objects.filter(user_id=userid, content_type_id=18, action_flag=1)
    for x in django_admin_object:
        django_admin_object_serialized = DjangoAdminLogSerializer(x)
        datapoints.append(django_admin_object_serialized.data['object_id'])

    serialized_data = {'datapoints': []}
    count = 0
    for x in datapoints:
        datapoints_object = Datapoints.objects.filter(id=x).first()
        if datapoints_object:
            datapoints_object_serialized = DatapointsSerializer(datapoints_object)
            serialized_data['datapoints'].append(datapoints_object_serialized.data)

    base = Path('dump')
    jsonpath = base / ('student_'+str(userid)+ '_' + str(username) + '.jsonld')

    try:
        base.mkdir(parents=True, exist_ok=True)
        jsonpath.write_text(json.dumps(serialized_data))
        # print(json.dumps(serialized_data))
        print("Completed: student_"+ str(userid) + '_' + str(username))
    except:
        print('Invalid JSON-LD')



