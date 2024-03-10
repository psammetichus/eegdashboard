from django.db import models

# Create your models here.

class Patient(models.Model):
    given = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.DateField()
    mrn = models.CharField(max_length=20)

class Recording(models.Model):
    patient = models.ForeignField("Patient", on_delete=models.CASCADE)
    start_epoch = DateTimeField()
    comments = models.CharField(max_length=250)

