from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Venue(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=520)
    zip_code=models.CharField(max_length=45)
    phone=models.CharField(max_length=45, blank=True)
    web_address=models.URLField(max_length=120,blank=True)
    email_address=models.EmailField(max_length=254,blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_name = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name + " "+ self.last_name
    

class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue=models.ForeignKey(Venue,null=True,blank=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    desc = models.TextField(blank=True)
    attendee =models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return self.name 


    