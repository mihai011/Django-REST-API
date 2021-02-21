from rest_framework import serializers
from .models import PowerRequest, FibonaciRequest, FactorialRequest, LogRequest

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerRequest
        fields = ('base', 'exponent', 'response')

class FibonaciSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibonaciRequest
        fields = ('index', 'response')

class FactorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorialRequest
        fields = ( 'index', 'response')

class LogRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogRequest
        fields = ('log',)