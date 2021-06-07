from django.contrib import admin
from django.urls import path
from djangoP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "homepage")
]