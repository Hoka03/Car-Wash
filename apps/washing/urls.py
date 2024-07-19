from django.urls import path

from .views import categories, carwashs


urlpatterns = [
    path('categories/', categories.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', categories.CategoryListCreateAPIView.as_view()),
    path('categories-items/', categories.CategoryRetrieveUpdateDeleteAPIView.as_view()),
    path('categories-items/<int:pk>/', categories.CategoryRetrieveUpdateDeleteAPIView.as_view()),
    # =========================         CAR WASH        ====================================
    path('car-wash/', carwashs.CarWashCreateListAPIView.as_view()),
    path('car-wash/<int:pk>/', carwashs.CarWashCreateListAPIView.as_view()),
    path('car-wash-items/', carwashs.CarWashUpdateDeleteApiView.as_view()),
    path('car-wash-items/<int:pk>/', carwashs.CarWashUpdateDeleteApiView.as_view()),
]