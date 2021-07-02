from django import forms
from django.forms import ModelForm
from accounts.models import User, CustomUser
from django.contrib.auth.forms import UserCreationForm
from common.models import Food, Order
from model_utils.fields import StatusField


class CreateRestaurantForm(UserCreationForm):
    phone = forms.IntegerField()
    location = forms.CharField()
    restaurant_name = forms.CharField()
    category = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'category', 'price', 'description', 'food_pic']


class ChangeOrderStatusForm(ModelForm):
    status = StatusField()

    class Meta:
        model = Order
        fields = ['status']





