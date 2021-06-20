from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .forms import AddFoodForm
from .models import Restaurant
from common.models import Food
from django.views import View

class RestaurantMainPage(View):

    def get(self, request):

        user_id = request.user.id
        restaurant = Restaurant.objects.get(user__user_id=user_id)
        context = {
            'restaurant': restaurant
        }
        return render(request, 'restaurantApp/restaurantMainPage.html', context)


class AddFood(View):

    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(user_id=restaurant_id)
        form = AddFoodForm()
        context = {
            'form': form,
            'restaurant': restaurant
        }
        return render(request, "restaurantApp/addFood.html", context)

    def post(self, request, restaurant_id):
        form = AddFoodForm(request.POST)

        if form.is_valid():
            food = form.save()
            restaurant = Restaurant.objects.get(user_id=restaurant_id)
            food.restaurant = restaurant
            food.save()

            context = {
                'restaurant': restaurant
            }

            return redirect('/')
        else:
            return redirect('/')

class RestaurantMenu(View):

    def get(self, request, pk):
        requested_restaurant = Restaurant.objects.get(user_id=pk)
        foods = Food.objects.filter(restaurant=requested_restaurant)
        context = {
            'restaurant': requested_restaurant,
            'foods': foods
        }
        return render(request, 'restaurantApp/restaurantMenu.html', context)



