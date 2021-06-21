from django.shortcuts import render
from django.views import View
from common.models import Food
from restaurantApp.models import Restaurant

class CustomerMainPage(View):

    def get(self, request):

        user_name = request.user.first_name
        all_restaurants = Restaurant.objects.all().order_by('restaurant_name')

        context = {
            'user_name' : user_name,
            'all_restaurants': all_restaurants
        }
        return render(request, 'customerApp/customerMainPage.html', context)

class OrderFood(View):

    def get(self, request, pk):

        food = Food.objects.get(pk=pk)
        context = {
            'food': food
        }
        return render(request,'customerApp/orderFood.html', context)





