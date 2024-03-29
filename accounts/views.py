from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from common.models import Order, Food
from accounts.models import CustomUser
from restaurant_operations.models import Restaurant
from customer_operations.models import Customer
from django.contrib import messages
from restaurant_operations.forms import CreateRestaurantForm
from customer_operations.forms import CreateCustomerForm, MakeCommentForm,MakeOrderForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request):
        return render(request, 'djangoP/home.html', {'name': 'Eat It!'});


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                uid = request.user.id
                print(uid)
                # restaurant login
                if get_user_type(uid) == 1:
                    return redirect('restaurant_main_page')
                # customer login
                else:
                    return redirect('customer_main_page')
            else:
                messages.info(request, 'invalid credentials')
                print('invalid credentials')
                return redirect('login')


# Returns:
# 1 if restaurant
# 2 if customer
def get_user_type(uid):
    if Restaurant.objects.filter(user=CustomUser.objects.get(user_id=uid)).exists():
        return 1
    else:
        return 2


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')


class RestaurantRegisterView(View):
    def get(self, request):
        form = CreateRestaurantForm()
        context = {
            'form': form
        }
        return render(request, "accounts/restaurant_register.html", context)

    def post(self, request):
        form = CreateRestaurantForm(request.POST)

        if form.is_valid():
            user = form.save()
            custom_user = CustomUser.objects.create(
                user=user,
                phone=form.cleaned_data["phone"],
                location=form.cleaned_data["location"],
            )
            restaurant = Restaurant.objects.create(
                user=custom_user,
                restaurant_name=form.cleaned_data["restaurant_name"],
                category=form.cleaned_data["category"],
            )
            user.save()
            restaurant.ordered_food_count = 0
            restaurant.save()
            return redirect('/accounts/login')
        else:
            return redirect('/')


class CustomerRegisterView(View):
    def get(self, request):
        form = CreateCustomerForm()
        context = {
            'form': form
        }
        return render(request, "accounts/customer_register.html", context)

    def post(self, request):
        form = CreateCustomerForm(request.POST)

        if form.is_valid():
            user = form.save()
            custom_user = CustomUser.objects.create(
                user=user,
                phone=form.cleaned_data["phone"],
                location=form.cleaned_data["location"],
            )
            customer = Customer.objects.create(
                user=custom_user,
                address=form.cleaned_data["address"]
            )
            user.save()
            customer.save()
            return redirect('/accounts/login')
        else:
            return redirect('/')


class ShowProfileView(LoginRequiredMixin, View):
    def get(self, request):
        # restaurant
        if (get_user_type(request.user.id) == 1):
            user = request.user
            custom_user = CustomUser.objects.get(user=user)
            restaurant = Restaurant.objects.get(user=custom_user)
            orders = Order.objects.filter(food__restaurant=restaurant)
            context = {
                'user': user,
                'custom_user': custom_user,
                'restaurant': restaurant,
                'orders': orders
            }
            return render(request, 'accounts/restaurant_show_profile.html', context)
        else:
            user = request.user
            custom_user = CustomUser.objects.get(user=user)
            customer = Customer.objects.get(user=custom_user)
            orders = Order.objects.filter(customer=customer)
            customer_form = CreateCustomerForm(instance=user)
            comment_form = MakeCommentForm()
            order_form = MakeOrderForm()

            context = {
                'user': user,
                'custom_user': custom_user,
                'form': customer_form,
                'orders': orders,
                'comment_form': comment_form,
                'order_form': order_form
            }
            return render(request, 'accounts/show_profile.html', context)


class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        customer = Customer.objects.get(user__user=user)
        customer_form = CreateCustomerForm(instance=user)
        context = {
            'user': user,
            'form': customer_form
        }
        return render(request, 'accounts/update_profile.html', context)

    def post(self, request):
        print(request.POST)
        user = request.user
        custom_user = CustomUser.objects.get(user=user)
        customer = Customer.objects.get(user=custom_user)
        customer_form = CreateCustomerForm(request.POST, instance=user)

        if customer_form.is_valid():
            customer_form.save()
            return redirect('show_profile')

        context = {
            'form': customer_form
        }
        return render(request, 'accounts/update_profile.html', context)


def index(request):
    return render(request, 'djangoP/index.html')

