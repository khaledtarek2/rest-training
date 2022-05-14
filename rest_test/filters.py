from django_filters import rest_framework as filters
from .models import Car

class CarFilter(filters.FilterSet):
    maker = filters.CharFilter(field_name='maker', lookup_expr='icontains')
    release_year = filters.NumberFilter(field_name='release_year', lookup_expr='release_year')
    release_year__gt = filters.NumberFilter(field_name='release_year', lookup_expr='release_year__gt')
    release_year__lt = filters.NumberFilter(field_name='release_year', lookup_expr='release_year__lt')
    vin = filters.CharFilter(field_name='vin', lookup_expr='icontains')

    
    
    class Meta:
        model = Car
        fields = ['maker', 'release_year', 'vin']
