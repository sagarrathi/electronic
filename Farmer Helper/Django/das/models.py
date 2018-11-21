from django.db import models

# Create your models here.
class ChartDb(models.Model):
    sd=models.IntegerField(null=True, blank=True )
    rtc=models.IntegerField(null=True, blank=True )
    dht=models.IntegerField(null=True, blank=True )
    year=models.IntegerField(null=True, blank=True )
    month=models.IntegerField(null=True, blank=True )
    day=models.IntegerField(null=True, blank=True )
    hour=models.IntegerField(null=True, blank=True )
    min=models.IntegerField(null=True, blank=True )
    sec=models.IntegerField(null=True, blank=True )
    # date_time=models.DateTimeField(null=True, blank=True)
    hum=models.IntegerField(null=True, blank=True )
    temp=models.IntegerField(null=True, blank=True )
    rain=models.IntegerField(null=True, blank=True )
    soil=models.IntegerField(null=True, blank=True )
    light=models.IntegerField(null=True, blank=True )
    hour_time=models.DateTimeField(null=True,blank=True)
    day_time=models.DateField(null=True,blank=True)
    full_time=models.BigIntegerField(null=True,blank=True)