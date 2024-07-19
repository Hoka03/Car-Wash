from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    class RoleChoices(models.IntegerChoices):
        DEV = 0, "Dev"
        DIRECTOR = 1, "Director"
        WASHER = 2, "Washer"

    role = models.PositiveSmallIntegerField(choices=RoleChoices.choices, default=RoleChoices.DEV.value)
    car_wash = models.ForeignKey('washing.CarWash', on_delete=models.CASCADE, blank=True, null=True)

    def clean(self):
        if self.RoleChoices == self.RoleChoices.WASHER.value and not self.car_wash:
            raise ValidationError({'car_wash': 'This field is required'})

    def __str__(self):
        return str(self.role)