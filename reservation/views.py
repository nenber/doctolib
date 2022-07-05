from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import TimeSlot
from .forms import CreateTimeSlot

from . import forms
# Create your views here.
def create_timeslot(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CreateTimeSlot(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "timeslot/create_timeslot.html", context)

def list_timeslot(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = TimeSlot.objects.all()
         
    return render(request, "timeslot/list_timeslot.html", context)

def backoffice(request):       
    return render(request, "backoffice.html")