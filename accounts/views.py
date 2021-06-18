from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views.generic import TemplateView

from accounts.models import UserModel
from restaurantApp.models import Restaurant
from customerApp.models import Customer
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserModelForm
from restaurantApp.forms import CreateRestaurantForm
from customerApp.forms import CreateCustomerForm
from django.views import View


def home(request):
    return render(request, 'djangoP/home.html', {'name': 'Pelin'});

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)

            uid = request.user.id
            print(uid)
            if get_user_type(uid) == 1: #restaurant login
                return redirect('restaurantMainPage')
            else:  #customer login
                return redirect('customerMainPage')

        else:
            messages.info(request, 'invalid credentials')
            print('invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

# Returns:
# 1 if restaurant
# 2 if customer
def get_user_type(uid):
    if Restaurant.objects.filter(user=UserModel.objects.get(user_id=uid)).exists():
        return 1
    else:
        return 2

def logout(request):
    auth.logout(request)
    return redirect('/')

class restaurantRegister(View):
    def get(self, request):
        form = CreateRestaurantForm()

        context = {
            'form': form
        }
        return render(request, "accounts/restaurantRegister.html", context)

    def post(self, request):
        form =CreateRestaurantForm(request.POST)

        if form.is_valid():
            user = form.save()
            usermodel = UserModel.objects.create(
                user=user,
                phone=form.cleaned_data["phone"],
                location=form.cleaned_data["location"],
            )
            restaurant = Restaurant.objects.create(
                user=usermodel,
                restaurant_name=form.cleaned_data["restaurant_name"],
                category=form.cleaned_data["category"],
                rate=0,
            )
            user.save()
            restaurant.save()
            return redirect('/accounts/login')
        else:
            return redirect('/')

class customerRegister(View):
    def get(self, request):
        form = CreateCustomerForm()

        context = {
            'form': form
        }
        return render(request, "accounts/customerRegister.html", context)

    def post(self, request):
        form =CreateCustomerForm(request.POST)

        if form.is_valid():
            user = form.save()
            usermodel = UserModel.objects.create(
                user=user,
                phone=form.cleaned_data["phone"],
                location=form.cleaned_data["location"],
            )
            customer = Customer.objects.create(
                user=usermodel,
                address=form.cleaned_data["address"]
            )
            user.save()
            customer.save()
            return redirect('/accounts/login')
        else:
            return redirect('/')

def index(request):
    return render(request, 'djangoP/index.html')
