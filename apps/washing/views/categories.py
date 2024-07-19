from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response

from apps.washing.serializers import CategorySerializers
from apps.washing.models import Category


class CategoryListCreateAPIView(APIView):
    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            many = False
        else:
            category = get_object_or_404(Category)
            many = True

        serializer = CategorySerializers(category, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            many = False
        else:
            category = get_object_or_404(Category)
            many = True

        serializer = CategorySerializers(category, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializers(instance=category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(category, status=status.HTTP_204_NO_CONTENT)
