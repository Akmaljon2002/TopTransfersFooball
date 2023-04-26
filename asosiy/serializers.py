from .models import *
from rest_framework import serializers

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

class Hozirgi_mavsumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hozirgi_mavsum
        fields = '__all__'