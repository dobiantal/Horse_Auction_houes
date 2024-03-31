from rest_framework import serializers
from Horse_images.models import Horse_images

class Horse_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse_images
        fields = '__all__'