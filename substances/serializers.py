""" serializers for substance data"""
from rest_framework import serializers
from substances.models import *


class ChemicalSerializer(serializers.ModelSerializer):
    """ identifiers serializer """
    class Meta:
        """ settings """
        model = Chemicals
        fields = '__all__'
        depth = 0


class IdentifierSerializer(serializers.ModelSerializer):
    """ identifiers serializer """
    class Meta:
        """ settings """
        model = Identifiers
        fields = '__all__'
        depth = 0


class SubstanceSerializer(serializers.ModelSerializer):
    """ substance serializer """
    ids = IdentifierSerializer(source='identifiers_set', many=True, required=False)
    chems = ChemicalSerializer(source='chemicals_set', many=True, required=False)

    class Meta:
        """ settings """
        model = Substances
        fields = '__all__'
        depth = 1
