from rest_framework import serializers
from Cities.models import Cities
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'