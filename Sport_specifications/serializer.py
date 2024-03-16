from rest_framework import serializers
from Sport_specifications.models import Sport_specification

class Sport_specSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_specification
        fileds = '__all__'