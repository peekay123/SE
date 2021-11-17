from django.db import models

# Create your models here.


class Events(models.Model):
    date = models.DateField()
    Event = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')


class Events2(models.Model):
    date = models.DateField()
    Event = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')


class Events1(models.Model):
    date = models.DateField()
    Event = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')


class Booking(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    field = models.CharField(max_length=250)
