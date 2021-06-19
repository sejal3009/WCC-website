from django.db import models
from django import forms

# Create your models here.
class Complaint (models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)

    email = models.EmailField()
    number = models.IntegerField()
    Date = models.DateField()
    complaint_type = models.CharField(max_length=50,null=True)
    detail_complaint = models.CharField(max_length=300)

    def __str__(self):
        return self.first + " " +self.last
