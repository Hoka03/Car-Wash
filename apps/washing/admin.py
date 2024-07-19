from django.contrib import admin

from .models import Category, CarWash


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}


@admin.register(CarWash)
class CarWashAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_categories', 'director')
    list_display_links = list_display
