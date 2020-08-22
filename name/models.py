from django.db import models

class cv(models.Model):
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    user = models.CharField(max_length=500)
    date_of_birth = models.DateField()
class mes(models.Model):
    user = models.CharField(max_length=500)
    fuser = models.CharField(max_length=1000)
class data(models.Model):
    fuserr = models.CharField(max_length=1000)
    owner = models.CharField(max_length=1000)
    masseage = models.CharField(max_length=10000)
class room(models.Model):
    user = models.CharField(max_length=500)
    croom = models.CharField(max_length=10000)
class up(models.Model):
    user = models.CharField(max_length=500)
    flag = models.CharField(max_length=100)
    updating = models.CharField(max_length=100)
      