from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.cars.models import Car
from apps.cars.serializers import CarSerializers


class CarCreateListAPIView(APIView):
    def post(self, request):
        serializer = CarSerializers(Car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            car = get_object_or_404(Car, pk=pk)
            many = False
        else:
            car = get_object_or_404(Car)
            many = True

        serializer = CarSerializers(car, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarUpdateDeleteAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            car = get_object_or_404(Car, pk=pk)
            many = False
        else:
            car = get_object_or_404(Car)
            many = True

        serializer = CarSerializers(car, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializers(instance=car, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        return Response(car, status=status.HTTP_204_NO_CONTENT)