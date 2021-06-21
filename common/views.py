from django.shortcuts import render





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
