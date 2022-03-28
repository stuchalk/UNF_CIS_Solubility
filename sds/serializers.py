""" serializers for reports data"""
from rest_framework import serializers
from sds.models import *


class QuantitySerializer(serializers.ModelSerializer):
    """ quantity serializer """

    class Meta:
        """ settings """
        model = Quantities
        fields = '__all__'
        depth = 1


class PropertySerializer(serializers.ModelSerializer):
    """ property serializer """
    quantity = QuantitySerializer(many=False, required=True)

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
        depth = 0
        exclude = ['dataset', 'dataseries']


class DatapointSerializer(serializers.ModelSerializer):
    """ datapoint serializer """
    conditions = ConditionSerializer(source='conditions_set', many=True, required=False)
    data = DataSerializer(source='data_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Datapoints
        fields = '__all__'
        depth = 0


class DataseriesSerializer(serializers.ModelSerializer):
    """ dataseries serializer """
    datapoints = DatapointSerializer(source='datapoints_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Dataseries
        fields = '__all__'
        depth = 0


class ChemicalSerializer(serializers.ModelSerializer):
    """ chemical serializer """

    class Meta:
        """ settings """
        model = Chemicals
        depth = 2
        exclude = ['report']


class IdentifierSerializer(serializers.ModelSerializer):
    """ identifiers serializer """

    class Meta:
        """ settings """
        model = Identifiers
        depth = 1
        exclude = ['substance']


class SubstanceSerializer(serializers.ModelSerializer):
    """ substance serializer """
    # chemical = ChemicalSerializer(source='chemicals_set', many=True, required=False)
    identifier = IdentifierSerializer(source='identifiers_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Substances
        fields = '__all__'
        depth = 2


class SystemSerializer(serializers.ModelSerializer):
    """ system serializer """
    # subsys = SubstanceSystemSerializer(source='substancessystems_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Systems
        depth = 2
        exclude = ['vol ']


class SubstanceSystemSerializer(serializers.ModelSerializer):
    """ substance_system serializer """
    substance = SubstanceSerializer()
    system = SystemSerializer()

    class Meta:
        """ settings """
        model = SubstancesSystems
        fields = '__all__'
        depth = 2


class DatasetSerializer(serializers.ModelSerializer):
    """ dataset serializer """
    dataseries = DataseriesSerializer(source='dataseries_set', many=True, required=False)
    # reference = ReferenceSerializer(many=False, required=True)
    system = SystemSerializer(many=False, required=False)

    class Meta:
        """ settings """
        model = Datasets
        depth = 3
        exclude = ['report']


class ReferencesReportsSerializer(serializers.ModelSerializer):
    """ references_reports serializer """
    class Meta:
        """ settings """
        model = ReferencesReports
        # fields = '__all__'
        exclude = ['report']
        depth = 2


class AuthorSerializer(serializers.ModelSerializer):
    """ authors serializer """

    class Meta:
        """ settings """
        model = Authors
        fields = '__all__'
        depth = 1


class AuthorReportSerializer(serializers.ModelSerializer):
    """ authors_reports serializer """

    class Meta:
        """ settings """
        model = AuthorsReports
        depth = 1
        exclude = ['report']


class ReportSerializer(serializers.ModelSerializer):
    """ reports serializer """
    set = DatasetSerializer(source='datasets_set', many=True, required=False)
    chem = ChemicalSerializer(source='chemicals_set', many=True, required=False)
    refs = ReferencesReportsSerializer(source='referencesreports_set', many=True, required=False)
    authrep = AuthorReportSerializer(source='authorsreports_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Reports
        fields = '__all__'
        depth = 2
