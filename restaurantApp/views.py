from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .forms import AddFoodForm
from .models import Restaurant
from django.contrib.auth.models import User
from django.views import View


# Create your views here.
def restaurant_main_page(request):
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
            restaurant = Restaurant.objects.get(id=restaurant_id)
            food.restaurant = restaurant
            food.save()

            context = {
                'restaurant': restaurant
            }

            return redirect('/')
        else:
            return redirect('/')



