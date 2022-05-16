from django_filters import rest_framework as filters
from .models import Car, Collection

class CarFilter(filters.FilterSet):
    maker = filters.CharFilter(field_name='maker', lookup_expr='icontains')
    from_release_year = filters.NumberFilter(field_name='release_year', lookup_expr='gte')
    to_release_year = filters.NumberFilter(field_name='release_year', lookup_expr='lte')
    vin = filters.CharFilter(field_name='vin', lookup_expr='icontains')
    collection = filters.CharFilter(field_name='collection', lookup_expr='icontains')
    
    class Meta:
        model = Car
        fields = ['maker', 'release_year', 'vin', 'collection']



class CollectionFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    created_at = filters.DateFilter(field_name='created_at')

    class Meta:
        model = Collection
        fields = ['name', 'created_at']