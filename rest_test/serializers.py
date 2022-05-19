from unicodedata import name
from rest_framework import serializers
from .models import Car, Collection, User

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'maker', 'release_year', 'vin', 'owner', 'collection']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'created_at']



class CarCollectionSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    collection = CollectionSerializer(many=True, required=False)
    
    class Meta:
        model = Car
        fields = ['id', 'model', 'maker', 'release_year', 'vin', 'owner', 'collection']
        read_only_fields = ['id', 'model', 'maker', 'release_year', 'vin', 'owner']
        



    
        
        

