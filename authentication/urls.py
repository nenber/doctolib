#users/urls.py

from django.urls import path

from . import views
urlpatterns = [

 path('', views.home, name = "home"),
 path("signup/", views.signup_page, name="signup"),
 path('profile/', views.profile, name='users_profile'),
 path("search/", views.SearchResultsView.as_view(), name="search_results")
]