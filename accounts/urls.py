from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name = 'register'),
    path('accounts/restaurantRegister', views.restaurantRegister.as_view(), name='restaurantRegister'),
    path('accounts/customerRegister', views.customerRegister.as_view(), name='customerRegister'),
    path('accounts/login', views.login, name = 'login'),
    path('accounts/logout', views.logout, name='logout')
]