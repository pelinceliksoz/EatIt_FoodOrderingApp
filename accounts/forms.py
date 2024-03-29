from django import forms
from .models import User,CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    phone = forms.CharField()
    location = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
