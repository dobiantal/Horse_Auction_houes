from rest_framework import serializers
from Beeders.models import Beeders
class BeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beeders
        fields = '__all__'