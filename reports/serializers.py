""" serializers for reports data"""
from rest_framework import serializers
from reports.models import *


class PropertySerializer(serializers.ModelSerializer):
    """ property serializer """

    class Meta:
        """ settings """
        model = Properties
        fields = '__all__'
        depth = 1


class UnitSerializer(serializers.ModelSerializer):
    """ unit serializer """

    class Meta:
        """ settings """
        model = Units
        fields = '__all__'
        depth = 0


class ConditionSerializer(serializers.ModelSerializer):
    """ condition serializer """
    property = PropertySerializer(many=False, required=True)
    unit = UnitSerializer(many=False, required=True)

    class Meta:
        """ settings """
        model = Conditions
        fields = '__all__'
        depth = 0


class DataSerializer(serializers.ModelSerializer):
    """ data serializer """
    property = PropertySerializer(many=False, required=True)
    unit = UnitSerializer(many=False, required=True)

    class Meta:
        """ settings """
        model = Data
        fields = '__all__'
        depth = 0


class DatapointSerializer(serializers.ModelSerializer):
    """ datapoint serializer """
    conditions = ConditionSerializer(source='conditions_set', many=True, required=False)
    data = DataSerializer(source='data_set', many=True, required=False)

    class Meta:
        """ datapoints """
        model = Datapoints
        fields = '__all__'
        depth = 0


class DataseriesSerializer(serializers.ModelSerializer):
    """ dataseries serializer """
    points = DatapointSerializer(source='datapoints_set', many=True, required=False)

    class Meta:
        """ dataseries """
        model = Dataseries
        fields = '__all__'
        depth = 0


class ChemicalSerializer(serializers.ModelSerializer):
    """ chemical serializer """

    class Meta:
        """ settings """
        model = Chemicals
        depth = 1
        exclude = ['rep']


class SubstanceSystemSerializer(serializers.ModelSerializer):
    """ substance_system serializer """

    class Meta:
        """ settings """
        model = SubstancesSystems
        fields = '__all__'
        depth = 2


class SubstanceSerializer(serializers.ModelSerializer):
    """ substance serializer """
    chemical = ChemicalSerializer(source='chemicals_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Substances
        fields = '__all__'
        depth = 0


class SystemSerializer(serializers.ModelSerializer):
    """ system serializer """
    subsys = SubstanceSystemSerializer(source='substances_systems_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Systems
        fields = '__all__'
        depth = 0


class ReferenceSerializer(serializers.ModelSerializer):
    """ reference serializer """

    class Meta:
        """ settings """
        model = References
        fields = '__all__'
        depth = 1


class DatasetSerializer(serializers.ModelSerializer):
    """ dataset serializer """
    series = DataseriesSerializer(source='dataseries_set', many=True, required=False)
    reference = ReferenceSerializer(many=False, required=True)
    system = SystemSerializer(source='systems_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Datasets
        depth = 3
        exclude = ['report']


class ReportSerializer(serializers.ModelSerializer):
    """ reports serializer """
    set = DatasetSerializer(source='datasets_set', many=True, required=False)
    chem = ChemicalSerializer(source='chemicals_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Reports
        fields = '__all__'
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    """ authors_reports serializer """

    class Meta:
        """ settings """
        model = Authors
        fields = '__all__'
        depth = 1


class AuthorReportSerializer(serializers.ModelSerializer):
    """ authors_reports serializer """
    auth = AuthorSerializer(source='authors_set', many=True, required=False)
    rep = ReportSerializer(source='reports_set', many=True, required=False)

    class Meta:
        """ settings """
        model = AuthorsReports
        fields = '__all__'
        depth = 0
