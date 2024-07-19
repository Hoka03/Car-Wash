from django.contrib import admin

from .models import Pricing


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'category', 'car_wash', 'price')
    list_display_links = list_display
