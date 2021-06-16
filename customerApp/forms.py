from django import forms
from accounts.models import User, UserModel
from django.contrib.auth.forms import UserCreationForm

class CreateCustomerForm(UserCreationForm):
    phone = forms.IntegerField()
    location = forms.CharField()
    address = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']




