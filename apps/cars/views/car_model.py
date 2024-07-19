from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarModelSerializers


class CarModelListCreateAPIView(APIView):
    def post(self, request):
        serializer = CarModelSerializers(CarModel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            car_model = get_object_or_404(CarModel, pk=pk)
            many = False
        else:
            car_model = get_object_or_404(CarModel)
            many = True
        serializer = CarModelSerializers(car_model, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarModelUpdateDeleteAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            car_model = get_object_or_404(CarModel, pk=pk)
            many = False
        else:
            car_model = get_object_or_404(CarModel)
            many = True
        serializer = CarModelSerializers(car_model, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)


def patch(self, request, pk):
    car_model = get_object_or_404(CarModel, pk=pk)
    serializer = CarModelSerializers(instance=car_model, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete(self, request, pk):
    car_model = get_object_or_404(CarModel, pk=pk)
    car_model.delete()
    return Response(car_model, status=status.HTTP_204_NO_CONTENT)
