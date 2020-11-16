from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Parasite


class ParasiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parasite
        fields = ['id', 'name', 'contaminationMethod', 'symptoms', 'protection', 'distribution']