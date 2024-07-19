from rest_framework import serializers

from apps.pricing.models import Pricing


class PricingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'