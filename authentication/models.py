from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipCity = models.CharField(max_length=10)
    phone =  models.CharField(max_length=10)
    job = models.CharField(max_length=100, null=True)
    descriptionDoctor = models.TextField(null=True)
    PATIENT = 'PATIENT'
    DOCTOR = 'DOCTOR'

    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Docteur'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
