from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from usuariomgc.models import UsuariomgcModel

class UsuariomgcSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariomgcModel
        fields = '__all__'
        # fields = ['id']