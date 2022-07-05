from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from .models import Reservation, TimeSlot
from .forms import CreateReservation, CreateTimeSlot
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from authentication.models import User
from django.template import RequestContext

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
    form = CreateTimeSlot(request.POST or None, initial={'doctor': request.user})
    if form.is_valid():
        form.save()
        return redirect('list-timeslot')

    context['form'] = form
    return render(request, "timeslot/create_timeslot.html", context)

@login_required
@user_passes_test(only_doctor)
def list_timeslot(request):
    user = request.user
    context ={}
    if request.user.role != 'DOCTOR':
        return redirect(settings.LOGIN_REDIRECT_URL)
    context["dataset"] = TimeSlot.objects.filter(doctor = user).order_by('slotStart')

    return render(request, "timeslot/list_timeslot.html", context)

@login_required
def doctor_timeslot(request, doctor_id=None):
    doctor = get_object_or_404(User, id=doctor_id)
    context ={}
    context["doctor"] = doctor
    context["dataset"] = TimeSlot.objects.filter(doctor = doctor).order_by('slotStart')
    context["cuurent_user"] = request.user
    return render(request, "timeslot/doctor_timeslot.html", context)

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

@login_required()
def create_reservation(request, doctor_id, patient_id, slot_id):
    patient = User.objects.get(pk=patient_id)
    doctor = User.objects.get(pk=doctor_id)
    slot = TimeSlot.objects.get(pk=slot_id)
    context = {
        'patient': patient,
        'doctor': doctor,
        'slot': slot
        }
    form = CreateReservation(request.POST or None, initial={
        'doctor': doctor,
        'patient': patient,
        'slot': slot
        })
    context['form'] = form
    if form.is_valid():
        form.save()
    slot.available = False
    slot.save()
    return render(request, "reservation/reservation.html", context)

@user_passes_test(only_doctor)
def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.delete()
    return redirect('list-reservation')

@user_passes_test(only_doctor)
def delete_timeslot(request, timeslot_id):
    timeSlot = TimeSlot.objects.get(pk=timeslot_id)
    timeSlot.delete()
    return redirect('list-timeslot')

def my_reservation(request):
    user = request.user
    context ={}


    context["dataset"] = Reservation.objects.filter(patient = user).order_by('slot__slotStart', 'slotStart')

    return render(request, "reservation/my_reservation.html", context)
