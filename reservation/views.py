from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
import reservation
# Create your views here.
def only_doctor(user):
     return user.role.endswith('DOCTOR')

@user_passes_test(only_doctor)
def create_timeslot(request):
    context ={}
    if request.user.role != 'DOCTOR':
        return redirect(settings.LOGIN_REDIRECT_URL)
    doctor = request.user.username
    form = CreateTimeSlot(request.POST or None, initial={'doctor': request.user})
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

@user_passes_test(only_doctor)
def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.delete()
    return redirect('list-reservation')
    # context ={}
    # # fetch the object related to passed id
    # obj = get_object_or_404(Reservation, id = id)
 
 
    # if request.method =="POST":
    #     obj.delete()
    #     return HttpResponseRedirect("/")
 
    # return render(request, "delete_reservation.html", context)