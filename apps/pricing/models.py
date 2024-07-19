from django.core.validators import MinValueValidator
from django.db import models


class Pricing(models.Model):
    car_model = models.ForeignKey('cars.CarModel', on_delete=models.PROTECT)
    category = models.ForeignKey('washing.Category', on_delete=models.PROTECT)
    car_wash = models.ForeignKey('washing.CarWash', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=1, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.car_model}: {self.price}"

    class Meta:
        unique_together =(('car_model', 'category', 'car_wash'),)
