from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import Reservation, TimeSlot
from .forms import CreateTimeSlot
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

from . import forms
# Create your views here.
def only_doctor(user):
     return user.role.endswith('DOCTOR')

@user_passes_test(only_doctor)
def create_timeslot(request):
    context ={}
    if request.user.role != 'DOCTOR':
        return redirect(settings.LOGIN_REDIRECT_URL)

    form = CreateTimeSlot(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "timeslot/create_timeslot.html", context)

@user_passes_test(only_doctor)
def list_timeslot(request):
    user = request.user
    context ={}
    if request.user.role != 'DOCTOR':
        return redirect(settings.LOGIN_REDIRECT_URL)
    context["dataset"] = TimeSlot.objects.filter(doctor = user).order_by('slotStart')

    return render(request, "timeslot/list_timeslot.html", context)

@user_passes_test(only_doctor)
def list_reservation(request):
    user = request.user
    context ={}
    if request.user.role != 'DOCTOR':
        return redirect(settings.LOGIN_REDIRECT_URL)

    context["dataset"] = Reservation.objects.filter(doctor = user).order_by('slot')

    return render(request, "reservation/list_reservation.html", context)

@user_passes_test(only_doctor)
def backoffice(request):
    if request.user.role != 'DOCTOR':       
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "backoffice.html")