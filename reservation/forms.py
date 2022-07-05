# authentication/forms.py

from django import forms

from authentication.models import User
from .models import Reservation, TimeSlot
 
class CreateTimeSlot(forms.ModelForm):
    doctor = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
    class Meta:
        model = TimeSlot
        fields = ('slotStart', 'slotEnd', 'doctor', 'available')

class CreateReservation(forms.ModelForm):
    slot = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=TimeSlot.objects.all())
    patient = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
    doctor = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
    class Meta:
        model = Reservation
        fields = ('patient', 'doctor', 'slot')
