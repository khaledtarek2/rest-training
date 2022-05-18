from django.db import models
from django.contrib.auth.models import User




    
    
class Collection(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name}"

    
class Car(models.Model):
    model = models.CharField(max_length=40)
    maker = models.CharField(max_length=60)
    release_year = models.IntegerField()
    vin = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    collection = models.ManyToManyField(Collection)
    
    
    def __str__(self):
        return f"{self.model}"