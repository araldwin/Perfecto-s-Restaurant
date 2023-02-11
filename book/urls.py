from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations', views.all_reservations, name="list-reservation"),
    path('add_reservation', views.add_reservation, name="add-reservation")
]
