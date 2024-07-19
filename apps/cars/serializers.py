from rest_framework import serializers

from .models import CarModel, Car, CarService


class CarModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarService
        fields = '__all__'
