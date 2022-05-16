from rest_framework import serializers
from .models import Car, Collection

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'maker', 'release_year', 'vin', 'owner', 'collection']
        
        
        def update(self, instance, validated_data):
            instance.model = validated_data.get('model', instance.model)
            instance.maker = validated_data.get('maker', instance.maker)
            instance.year = validated_data.get('release_year', instance.release_year)
            instance.vin = validated_data.get('vin', instance.vin)
            return instance
        

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'created_at']
