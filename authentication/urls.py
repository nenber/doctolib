#users/urls.py

from django.urls import path


from . import views
urlpatterns = [

 path('', views.home, name = "home"),
 path("signup/", views.signup_page, name="signup"),
 path('profile/<int:user_id>/', views.profile, name='users_profile'),
 path('edit-profile/', views.edit_profile, name='users_profile'),
 path("search/", views.SearchResultsView.as_view(), name="search_results"),
 path("complete-profile/", views.complete_profile_doctor, name="complete_profile")

]