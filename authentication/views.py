from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.
def home(request):
    return render(request,"users/home.html")

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'users/signup.html', context={'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')