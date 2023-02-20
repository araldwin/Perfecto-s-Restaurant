from django.urls import path, include
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<slug:slug>', views.menu_detail, name='menu_detail')
]
