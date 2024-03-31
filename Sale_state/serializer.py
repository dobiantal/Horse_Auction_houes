from rest_framework import serializers
from Sale_state.models import Sale_state

class Sale_stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale_state
        fields = '__all__'