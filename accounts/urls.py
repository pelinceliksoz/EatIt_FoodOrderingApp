from django.urls import path, include

import customerApp
import restaurantApp
from . import views
from restaurantApp import urls
from customerApp import urls

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name ='index'),
    path('accounts/restaurantRegister', views.restaurantRegister.as_view(), name='restaurantRegister'),
    path('accounts/customerRegister', views.customerRegister.as_view(), name='customerRegister'),
    path('accounts/login', views.login, name = 'login'),
    path('accounts/logout', views.logout, name='logout'),
    path('restaurantApp/', include(restaurantApp.urls)),
    path('customerApp/', include(customerApp.urls))

]