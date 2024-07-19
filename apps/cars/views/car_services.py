from django.shortcuts import get_object_or_404

from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.cars.models import CarService
from apps.cars.serializers import CarServiceSerializers


class CarServiceCreateListAPIView(APIView):
    def post(self, request):
        serializer = CarServiceSerializers(CarService, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            car_service = get_object_or_404(CarService, pk=pk)
            many = False
        else:
            car_service = get_object_or_404(CarService)
            many = True

        serializer = CarServiceSerializers(car_service, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarServiceUpdateDeleteAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            car_service = get_object_or_404(CarService, pk=pk)
            many = False
        else:
            car_service = get_object_or_404(CarService)
            many = True

        serializer = CarServiceSerializers(car_service, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        car_service = get_object_or_404(CarService, pk=pk)
        serializer = CarServiceSerializers(instance=car_service, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car_service = get_object_or_404(CarService, pk=pk)
        car_service.delete()
        return Response(car_service, status=status.HTTP_204_NO_CONTENT)