from django.contrib import admin

from apps.cars.models import CarModel, Car, CarService


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('number', 'model')
    list_display_links = list_display


@admin.register(CarService)
class CarServiceAdmin(admin.ModelAdmin):
    list_display = ('pricing', 'washer')
    list_display_links = list_display
