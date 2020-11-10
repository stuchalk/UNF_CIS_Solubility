""" Create your tests here. """
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from django.core import serializers
from substances.models import *
from substances.serializers import *

compound = SubstanceSerializer(Substances.objects.get(name__iexact='ammonia'))
print(json.dumps(compound.data, indent=2))
