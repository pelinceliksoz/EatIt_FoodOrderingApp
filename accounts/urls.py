from django.urls import path, include
import customer_operations
import restaurant_operations
import common
from . import views
from restaurant_operations import urls
from customer_operations import urls
from common import urls

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('index', views.index, name='index'),
    path('accounts/restaurant_register', views.RestaurantRegisterView.as_view(), name='restaurant_register'),
    path('accounts/customer_register', views.CustomerRegisterView.as_view(), name='customer_register'),
    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('accounts/logout', views.LogoutView.as_view(), name='logout'),
    path('restaurant_operations/', include(restaurant_operations.urls)),
    path('customer_operations/', include(customer_operations.urls)),
    path('accounts/show_profile', views.ShowProfileView.as_view(), name='show_profile'),
    path('accounts/update_profile', views.UpdateProfileView.as_view(), name='update_profile'),
    path('common/', include(common.urls))

]