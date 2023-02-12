from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation_list', views.list_reservation, name="list-reservation"),
    path('show_reservation/<reservation_id>', views.show_reservation, name='show-reservation'),
    path('update_reservation/<reservation_id>', views.update_reservation, name='update-reservation'),
    path('add_reservation', views.add_reservation, name="add-reservation"),
    path('delete_reservation/<reservation_id>', views.delete_reservation, name='delete-reservation'),
]
