#users/urls.py

from django.urls import path

from . import views
urlpatterns = [
 path("create-timeslot/", views.create_timeslot, name="create-timeslot"),
  path("list-timeslot/", views.list_timeslot, name="list-timeslot"),
  path("", views.backoffice, name="backoffice"),
  path("list-reservation/", views.list_reservation, name="list-reservation"),
  path('delete-reservation/<reservation_id>', views.delete_reservation, name="delete-reservation" ),
  path('delete-timeslot/<timeslot_id>', views.delete_timeslot, name="delete-timeslot" ),
]