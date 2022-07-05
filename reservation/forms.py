# authentication/forms.py

from django import forms

from authentication.models import User
from .models import TimeSlot
 
class CreateTimeSlot(forms.ModelForm):
    doctor = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
    class Meta:
        model = TimeSlot
        fields = ('slotStart', 'slotEnd', 'doctor', 'available')
