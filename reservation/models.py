from django.db import models
from django.forms import BooleanField

# Create your models here.
class Reservation(models.Model):
    description = models.TextField()
    # ManyToOne
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor  = models.ForeignKey(User, on_delete=models.CASCADE)
    # OneToOne
    slot = models.OneToOneField(
        TimeSlot,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class TimeSlot(models.Model): 
    slotStart = models.DateField()
    slotEnd = models.DateField()
    # ManyToOne
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField()