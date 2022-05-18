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
    model = serializers.CharField(read_only=True)
    maker = serializers.CharField(read_only=True)
    release_year = serializers.IntegerField(read_only=True)
    vin = serializers.CharField(read_only=True)
    owner = UserSerializer(read_only=True)
    
    
    class Meta:
        model = Car
        fields = ['id', 'model', 'maker', 'release_year', 'vin', 'owner', 'collection']


