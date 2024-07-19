from django.urls import path

from apps.cars.views import car_model, car, car_services


urlpatterns = [
    path('car-model/', car_model.CarModelListCreateAPIView.as_view()),
    path('car-model/<int:pk>/', car_model.CarModelListCreateAPIView.as_view()),
    path('car-model/', car_model.CarModelUpdateDeleteAPIView.as_view()),
    path('car-model/<int:pk>/', car_model.CarModelUpdateDeleteAPIView.as_view()),
    # ============================ CAR ===========================================
    path('car/', car.CarCreateListAPIView.as_view()),
    path('car/<int:pk>/', car.CarCreateListAPIView.as_view()),
    path('car/', car.CarUpdateDeleteAPIView.as_view()),
    path('car/<int:pk>/', car.CarUpdateDeleteAPIView.as_view()),
    # ============================ CAR SERVICE ====================================
    path('car-service/', car_services.CarServiceCreateListAPIView.as_view()),
    path('car-service/<int:pk>/', car_services.CarServiceCreateListAPIView.as_view()),
    path('car-service/', car_services.CarServiceUpdateDeleteAPIView.as_view()),
    path('car-service/<int:pk>/', car_services.CarServiceUpdateDeleteAPIView.as_view()),
]
