from django.db import models
from django.conf import settings

from .validators import validate_car_number


class CarModel(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.parent}'


class Car(models.Model):
    number = models.CharField(max_length=8, validators=[validate_car_number])
    model = models.ForeignKey(CarModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.number + ' ' + self.model


class CarService(models.Model):
    pricing = models.ForeignKey('pricing.Pricing', on_delete=models.PROTECT)
    washer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.washer, self.pricing)