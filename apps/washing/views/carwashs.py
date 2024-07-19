from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from apps.washing.models import CarWash
from apps.washing.serializers import CarWashSerializers


class CarWashCreateListAPIView(APIView):
    def post(self, request):
        serializer = CarWashSerializers(CarWash, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk is None:
            car_wash = CarWash.objects.all()
            serializer = CarWashSerializers(car_wash, many=True)
        else:
            car_wash = get_object_or_404(CarWash, pk=pk)
            serializer = CarWashSerializers(car_wash)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarWashUpdateDeleteApiView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            car_wash = CarWash.objects.all()
            serializer = CarWashSerializers(car_wash, many=True)
        else:
            car_wash = get_object_or_404(CarWash, pk=pk)
            serializer = CarWashSerializers(car_wash)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        car_wash = get_object_or_404(CarWash, pk=pk)
        serializer = CarWashSerializers(instance=car_wash, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car_wash = get_object_or_404(CarWash, pk=pk)
        car_wash.delete()
        return Response(car_wash, status=status.HTTP_204_NO_CONTENT)