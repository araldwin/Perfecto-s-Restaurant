from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation_list', views.list_reservation, name="list-reservation"),
    path('show_reservation/<reservation_id>', views.show_reservation, name='show-reservation'),
    path('add_reservation', views.add_reservation, name="add-reservation"),
]
