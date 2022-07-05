from ast import arg
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView

from authentication.models import User

from . import forms

# Create your views here.
def home(request):
    return render(request,"users/home.html")

def signup_page(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            if request.user.role == 'PATIENT': 
                return redirect(settings.LOGIN_REDIRECT_URL)
            if request.user.role == 'DOCTOR': 
                return redirect('http://127.0.0.1:8000/complete-profile/')
    return render(request, 'users/signup.html', context={'form': form})

@login_required
def complete_profile_doctor(request):
    current_user = request.user
    form = forms.CompleteProfileDoctor(request.POST or None, instance=current_user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
            # auto-login user
    return render(request, 'doctor/complete_profile_doctor.html', context={'form': form})

@login_required
def profile(request, user_id=None):
    if user_id:
        profile_owner = get_object_or_404(User, id=user_id)
    else:
        profile_owner = request.user
    args = {
        'profile_owner': profile_owner
    }
    return render(request, 'users/profile.html', args)

@login_required
def edit_profile(request):
    current_user = request.user
    form = forms.EditProfile(request.POST or None, instance=current_user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'users/edit_profile.html', {'form': form})

class SearchResultsView(ListView):
    model = User
    template_name = 'users/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return User.objects\
        .filter(role__icontains="doctor")\
        .filter(
            Q(city__icontains=query) | Q(job__icontains=query)
        )