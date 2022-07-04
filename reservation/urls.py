#users/urls.py

from django.urls import path

from . import views
urlpatterns = [
 path("create-timeslot/", views.create_timeslot, name="create-timeslot"),
  path("list-timeslot/", views.list_timeslot, name="list-timeslot"),
]