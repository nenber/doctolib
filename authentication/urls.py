#users/urls.py

from django.urls import path

from . import views
urlpatterns = [

 path('', views.home, name = "home"),
 path("signup/", views.signup_page, name="signup"),
]