# authentication/forms.py

from django import forms

from authentication.models import User
from .models import TimeSlot
 
class CreateTimeSlot(forms.ModelForm):
    # slotStart = forms.DateField(required=True)
    # slotEnd = forms.DateField(required=True)
    # available = forms.BooleanField(required=True)
    doctor = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
    class Meta:
        model = TimeSlot
        fields = ('slotStart', 'slotEnd', 'doctor', 'available')
