from django.db import models
from rest_framework import serializers


class Car(models.Model):
    model = models.CharField(max_length=40)
    maker = models.CharField(max_length=60)
    year = models.IntegerField()
    vin = models.CharField(max_length=100)
    
    

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'maker', 'year', 'vin']