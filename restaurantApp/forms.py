from django import forms
from accounts.models import User, UserModel
from django.contrib.auth.forms import UserCreationForm

class CreateRestaurantForm(UserCreationForm):
    phone = forms.IntegerField()
    location = forms.CharField()
    category = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']




