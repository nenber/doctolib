from django.db import models
from django.forms import BooleanField

from authentication.models import User

# Create your models here.
class TimeSlot(models.Model): 
    slotStart = models.DateField()
    slotEnd = models.DateField()
    # ManyToOne
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField()
class Reservation(models.Model):
    description = models.TextField()
    # ManyToOne
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    doctor  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    # OneToOne
    slot = models.OneToOneField(
        TimeSlot,
        on_delete=models.CASCADE,
        primary_key=True,
    )