from django.db import models

# Create your models here.

class Persons(models.Model):
    PersonID  = models.IntegerField(primary_key=True)
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=10)

    def __str__(self):
        return self.FirstName
 
class NagStudent(models.Model):
    st_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    sc_name = models.CharField(max_length=20)
    def __str__(self):
        return self.firstname

