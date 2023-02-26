from django.urls import path
from . import views
from .views import food_detail

app_name = 'food'

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('<slug:slug>/', views.food_detail, name='food_detail'),
]
