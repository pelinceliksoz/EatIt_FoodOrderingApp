from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name = 'register'),
    path('accounts/login', views.login, name = 'login'),
    path('accounts/restaurantMainPage', views.restaurantMainPage, name = 'restaurantMainPage'),
    path('accounts/logout', views.logout, name='logout')
]