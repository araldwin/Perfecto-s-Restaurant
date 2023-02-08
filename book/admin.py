from django.contrib import admin
from .models import Branch
from .models import MyRestaurantUser
from .models import Book


admin.site.register(Branch)
admin.site.register(MyRestaurantUser)
admin.site.register(Book)
