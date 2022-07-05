# authentication/forms.py

from django import forms
from .models import TimeSlot
 
class CreateTimeSlot(forms.ModelForm):
    # slotStart = forms.DateField(required=True)
    # slotEnd = forms.DateField(required=True)
    # available = forms.BooleanField(required=True)

    class Meta:
        model = TimeSlot
        fields = ('slotStart', 'slotEnd', 'doctor', 'available')