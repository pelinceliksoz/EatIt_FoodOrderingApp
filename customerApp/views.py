from django.shortcuts import render
from restaurantApp.models import Restaurant
from django.contrib.auth.models import User

# Create your views here.
def customerMainPage(request):

    user_name = request.user.first_name
    all_restaurants = Restaurant.objects.all().order_by('restaurant_name')

    #restaurants = Restaurant.objects.all()
    context = {
        'user_name' : user_name,
        'all_restaurants': all_restaurants
    }
    return render(request, 'customerApp/customerMainPage.html', context)





