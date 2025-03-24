from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from huella.models import HuellaModel

class HuellaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuellaModel
        fields = '__all__'
        # fields = ['id']