#users/urls.py

from django.urls import path

from . import views
urlpatterns = [
  path("create-timeslot/", views.create_timeslot, name="create-timeslot"),
  path("list-timeslot/", views.list_timeslot, name="list-timeslot"),
  path("", views.backoffice, name="backoffice"),
  path("list-reservation/", views.list_reservation, name="list-reservation"),
  path("<int:doctor_id>/timeslot", views.doctor_timeslot, name="doctor-timeslot"),
]