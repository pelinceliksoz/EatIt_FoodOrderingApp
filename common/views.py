from django.shortcuts import render
from restaurant_operations.models import Restaurant


def searchRestaurant(request):
    restaurant_name = request.session['restaurant_name']
    context = {
        'restaurant_name': restaurant_name
    }
    restaurant_arr = []
    if request.method == "POST":
        searched = request.POST['searched']
        all_restaurants = Restaurant.objects.all()

        for restaurant in all_restaurants:
            if str(restaurant.__getitem__(1)).lower().__eq__(str(searched).lower()):
                context = {'restaurant': restaurant, 'restaurant_name': restaurant_name}
                return render(request, 'restaurant_operations/restaurant_menu.html', context)
            elif str(restaurant.__getitem__(1)).lower().__contains__(str(searched).lower()):
                restaurant_arr.append(restaurant)
                context = {'searched': searched, 'restaurants': restaurant_arr, 'restaurant_name': restaurant_name}
                return render(request, 'common/search_restaurant.html', context)
            else:
                return render(request, 'common/search_restaurant.html', context)

# def searchCourse(request):
#     uname = request.session['username']
#     context = {'username': uname}
#     courseArr = []
#     if request.method == "POST":
#         searched = request.POST['searched']
#         all_courses = get_all_courses()
#
#         for course in all_courses:
#             if str(course.__getitem__(1)).lower().__eq__(str(searched).lower()):
#                 context = {'course': course, 'username': uname}
#                 return render(request, 'PeakyLearn/courseDetails.html', context)
#             elif str(course.__getitem__(1)).lower().__contains__(str(searched).lower()):
#                 courseArr.append(course)
#                 context = {'searched': searched, 'courses': courseArr, 'username': uname}
#                 (request, 'PeakyLearn/searchCourse.html', context)
#         return render(request, 'PeakyLearn/searchCourse.html', context)
#     else:
#         return render(request, 'PeakyLearn/searchCourse.html', context)
