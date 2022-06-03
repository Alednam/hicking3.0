from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class Contact(models.Model):
    hiking= models.CharField(max_length=200)
    hiking_id=models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name