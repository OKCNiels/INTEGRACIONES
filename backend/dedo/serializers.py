from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from dedo.models import DedoModel

class DedoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DedoModel
        fields = '__all__'
        # fields = ['id']