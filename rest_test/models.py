from django.db import models



class Car(models.Model):
    model = models.CharField(max_length=40)
    maker = models.CharField(max_length=60)
    year = models.IntegerField()
    vin = models.CharField(max_length=100)
    
    

