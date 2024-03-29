from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('restaurant_main_page', views.RestaurantMainPageView.as_view(), name='restaurant_main_page'),
    path('add_food/<int:restaurant_id>/', views.AddFoodView.as_view(), name='add_food'),
    path('restaurant_menu/<int:pk>/', views.RestaurantMenuView.as_view(), name='restaurant_menu'),
    path('update_food/<int:pk>/', views.UpdateFoodView.as_view(), name='update_food'),
    path('delete_food/<int:pk>/', views.DeleteFoodView.as_view(), name='delete_food'),
    path('restaurant_show_orders', views.RestaurantShowOrdersView.as_view(), name='restaurant_show_orders'),
    path('change_order_status/<int:pk>/', views.ChangeOrderStatusView.as_view(), name='change_order_status'),
    path('restaurant_likes_comments', views.RestaurantLikeComments.as_view(), name='restaurant_likes_comments'),
    path('restaurant_food_details/<int:pk>/', views.RestaurantFoodDetails.as_view(), name='restaurant_food_details'),
    path('restaurant_customer_profile/<int:pk>/', views.RestaurantCustomerProfile.as_view(), name='restaurant_customer_profile'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)