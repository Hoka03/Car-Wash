from rest_framework import serializers

from .models import Category, CarWash


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CarWashSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarWash
        fields = '__all__'


