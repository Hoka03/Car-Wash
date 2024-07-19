from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response

from apps.pricing.models import Pricing
from apps.pricing.serializers import PricingSerializers


class PricingCreateListAPIView(APIView):
    def post(self, request):
        serializer = PricingSerializers(Pricing, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            price = get_object_or_404(Pricing, pk=pk)
            many = False
        else:
            price = get_object_or_404(Pricing)
            many = True

        serializer = PricingSerializers(price, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PricingUpdateDeleteAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            price = get_object_or_404(Pricing, pk=pk)
            many = False
        else:
            price = get_object_or_404(Pricing)
            many = True

        serializer = PricingSerializers(price, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        price = get_object_or_404(Pricing, pk=pk)
        serializer = PricingSerializers(instance=price, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        price = get_object_or_404(Pricing, pk=pk)
        price.delete()
        return Response(price, status=status.HTTP_204_NO_CONTENT)
