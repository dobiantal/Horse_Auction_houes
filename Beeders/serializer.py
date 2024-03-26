from rest_framework import serializers
from Beeders.models import Beeders
class BeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beeders
        fields = ['id','Beeder_F_name','Beeder_L_name','Stable_name','Beeder_phone','Beeder_email','Beeder_webpage']