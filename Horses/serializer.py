from rest_framework import serializers
from Horses.models import Horse
from Horse_images.serializer import Horse_imagesSerializer
from Sport_specifications.serializer import Sport_specSerializer
from Sale_state.serializer import Sale_stateSerializer
from Beeders.serializer import BeederSerializer
from Bidder.serializer import BidderSerializer
class HorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse
        fields = '__all__'

class AllSerializer(serializers.ModelSerializer):
    images = Horse_imagesSerializer(many=True)
    sport = Sport_specSerializer(many=True)
    sale = Sale_stateSerializer(many=True)
    breeder = BeederSerializer(many=True)
    bidder = BidderSerializer(many=True)
    class Meta:
        model = Horse
        fields = '__all__'