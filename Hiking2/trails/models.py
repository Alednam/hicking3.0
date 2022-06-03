from django.db import models

# Create your models here.
#from django.db.models.functions import datetime
from mguides.models import Mguide
from datetime import datetime

class Hike(models.Model):
    mguide = models.ForeignKey(Mguide, on_delete=models.DO_NOTHING)
    #location
    title = models.CharField(max_length=100)
    distance_from_Nairobi=models.IntegerField(blank=True)
    trail_length =models.IntegerField(blank=True)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    departure_time = models.TimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    rendezvous_point= models.CharField(max_length=100)
    difficulty_mode=models.CharField(max_length=100)
    date_of_hike=models.DateTimeField(default=datetime.now,blank=True)
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published= models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title