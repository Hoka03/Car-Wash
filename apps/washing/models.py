from django.db import models
from django.conf import settings

from apps.users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CarWash(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    director = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 limit_choices_to={'role': CustomUser.RoleChoices.DIRECTOR.value})

    def __str__(self):
        return self.name

    def display_categories(self):
        return ', '.join(category.name for category in self.categories.all())
