from django.urls import path
from . import views

urlpatterns = [
    path('customerMainPage', views.CustomerMainPage.as_view(), name='customerMainPage'),
    path('orderFood/<int:pk>/', views.OrderFood.as_view(), name='orderFood'),
]