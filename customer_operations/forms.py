from django import forms
from accounts.models import User
from common.models import Comment
from django.contrib.auth.forms import UserCreationForm

from customer_operations.models import Customer


class CreateCustomerForm(UserCreationForm):
    phone = forms.IntegerField()
    location = forms.CharField()
    address = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class MakeCommentForm(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = Comment
        fields = ['content']
