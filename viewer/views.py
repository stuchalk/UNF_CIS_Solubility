
# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")
# django.setup()
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from rest_framework import serializers
from viewer.inspectdb import *
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


def view(request, user_id):
    """ show data about a specific report """
    datapoints = []
    django_admin_object = DjangoAdminLog.objects.filter(user_id=user_id, content_type_id=18, action_flag=1)
    for x in django_admin_object:
        django_admin_object_serialized = DjangoAdminLogSerializer(x)
        datapoints.append(django_admin_object_serialized.data['object_id'])

    serialized_data = {'datapoints': []}
    for x in datapoints:
        datapoints_object = Datapoints.objects.filter(id=x).first()
        if datapoints_object:
            datapoints_object_serialized = DatapointsSerializer(datapoints_object)
            serialized_data['datapoints'].append(datapoints_object_serialized.data)
    student_data = json.dumps(serialized_data, indent=4)

    return render(request, "../templates/viewer/view.html",
                  {'student_data': student_data, 'user_id': user_id})
