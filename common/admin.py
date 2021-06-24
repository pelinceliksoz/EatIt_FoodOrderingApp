from django.contrib import admin
from .models import Food
from  .models import Comment

admin.site.register(Food)
admin.site.register(Comment)
