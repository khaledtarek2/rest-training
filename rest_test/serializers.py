from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'maker', 'year', 'vin']
        
        
        def update(self, instance, validated_data):
            instance.model = validated_data.get('model', instance.model)
            instance.maker = validated_data.get('maker', instance.maker)
            instance.year = validated_data.get('year', instance.year)
            instance.vin = validated_data.get('vin', instance.vin)
            return instance