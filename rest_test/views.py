from telnetlib import STATUS
from rest_framework.response import Response
from .models import Car, Collection
from .serializers import CarSerializer, CollectionSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from .filters import CarFilter, CollectionFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCarOwner
        

class CarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving cars.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, IsCarOwner]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class =  CarFilter
    filter_fields = ('maker', 'release_year', 'vin')
    ordering_fields = 'release_year'
    
    @action(detail=True, methods=['Put'])
    def add_to_collection(self, request, pk=None, format=None):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['Put'])
    def remove_from_collection(self, request, pk=None, format=None):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    

        
class CollectionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving cars.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class =  CollectionFilter
    filter_fields = ('name', 'created_at', 'cars')
    ordering_fields = 'created_at'
    
    
 
    
   
        
        

    


    # def add_to_collection(self, request, pk=None, format=None):
    #     car = get_object_or_404(Car, pk=pk)
    #     serializer = CarSerializer(car)
    #     collection_serializer = CollectionSerializer(Collection, request.data)
    #     return Response(collection_serializer.data)
    
    

# class CarViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving cars.
#     """
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_class =  (CarFilter,)
#     filter_fields = ('maker', 'release_year', 'vin')
#     ordering_fields = ('release_year')
    

#     def list(self, request, format=None):
#         serializer = CarSerializer(self.queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, pk=None,format=None):
#         car = get_object_or_404(self.queryset, pk=pk)
#         serializer = CarSerializer(car)
#         return Response(serializer.data)


#     def create(self, request, format=None):
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
        
        

#     def update(self, request, pk=None, format=None):
#         car = get_object_or_404(Car, pk=pk)
#         serializer = CarSerializer(car, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
       
       
