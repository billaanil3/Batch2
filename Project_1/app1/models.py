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

# 1. O2O
# 2. O2M
# 3. M2O
# 4. M2M

# One To Many
class Menu(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# class Item(models.Model):
#     name = models.CharField(max_length=30)
#     description = models.CharField(max_length=100)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

# Many To Many
class Amenity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=30)    
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return self.name

# One To One
class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    calories = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Drink(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.item

