from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render
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