from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('restaurantMainPage', views.restaurantMainPage, name = 'restaurantMainPage'),
    path('logout', views.logout, name='logout')
]