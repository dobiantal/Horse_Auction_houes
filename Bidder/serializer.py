from rest_framework import serializers
from Bidder.models import Bidder
class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = '__all__'