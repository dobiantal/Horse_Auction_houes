from rest_framework import serializers
from Bidder.models import Bidder
from django.contrib.auth.hashers import make_password
class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = '__all__'
    def create(self, validated_data):
        password = validated_data.pop('Password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.Password = make_password(password)
            instance.save()
        return instance
    """In this method change the password to hash code."""