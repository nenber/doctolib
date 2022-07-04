from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
    adress = models.TextField()
    city = models.TextField()
    zipCity = models.TextField()
    phone =  models.TextField()
    job = models.TextField(null=True)
    descriptionDoctor = models.TextField(null=True)
    PATIENT = 'PATIENT'
    DOCTOR = 'DOCTOR'

    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Docteur'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
