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
from .forms import UserCreationForm


def home(request):
    return render(request, 'home.html', {'name' : 'Pelin'});

def restaurantRegister(request):
    return render(request, 'accounts/restaurantRegister.html')

def customerRegister(request):
    return render(request, 'accounts/customerRegister.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']

        if(password1==password2):
            if User.objects.filter(username=username).exists():
                #messages.info(request,'Username Taken')
                print('username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                #messages.info(request,'Email Taken')
                print('email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matched')
            print('password not matched')
        return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            #return render(request, 'customerApp/customerMainPage.html')
            return render(request,'restaurantApp/restaurantMainPage.html')
        else:
            messages.info(request, 'invalid credentials')
            print('invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

class restaurantRegister(TemplateView):
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
            return render(request, 'restaurantApp/restaurantMainPage.html')
        else:
            return redirect('/')

class customerRegister(TemplateView):
    def get(self, request):
        form = UserModelForm()

        context = {
            'form': form
        }
        return render(request, "accounts/customerRegister.html", context)

    def post(self, request):
        form =UserModelForm(request.POST)

        if form.is_valid():
            user = form.save()
            usermodel = UserModel.objects.create(
                user=user,
                phone=form.cleaned_data["phone"],
                location=form.cleaned_data["location"],
            )
            customer = Customer.objects.create(
                user=usermodel,
            )
            user.save()
            customer.save()
            return render(request, 'customerApp/customerMainPage.html')
        else:
            return redirect('/')