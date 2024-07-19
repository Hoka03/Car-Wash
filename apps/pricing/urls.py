from django.urls import path

from .views import PricingCreateListAPIView, PricingUpdateDeleteAPIView


urlpatterns = [
    path('price/', PricingCreateListAPIView.as_view()),
    path('price/<int:pk>/', PricingCreateListAPIView.as_view()),
    path('price/', PricingUpdateDeleteAPIView.as_view()),
    path('price/<int:pk>/', PricingUpdateDeleteAPIView.as_view()),
]