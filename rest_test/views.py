from telnetlib import STATUS
from rest_framework.response import Response
from .models import Car, Collection, User
from .serializers import CarSerializer, CollectionSerializer, CarCollectionSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from .filters import CarFilter, CollectionFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCarOwner
from rest_framework.renderers import JSONRenderer


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
    
    @action(detail=True, methods=['GET', 'Put'])
    def update_car_collection(self, request, pk=None, format=None):
        car = Car.objects.get(pk=pk)
        serializer = CarCollectionSerializer(car, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    @action(detail=True, methods=['GET', 'Put'])
    def add_to_collection(self, request, pk=None, format=None):
        car = Car.objects.get(pk=pk)
        collectionss = Collection.objects.get(pk=pk)
        serializer = CarCollectionSerializer(car, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    @action(detail=True, methods=['GET', 'Put'])
    def remove_from_collection(self, request, pk=None, format=None):
        car = Car.objects.get(pk=pk)
        serializer = CarCollectionSerializer(car, request.data)
        serializer.delete(car, request.data, pk=pk)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





    # @action(detail=True, methods=['GET', 'Put'])
    # def update_car_collection(self, request, pk=None, format=None, partial=True):
    #     car = Car.objects.get(pk=pk)
    #     car.model = request.data.get('model', car.model)
    #     car.maker = request.data.get('maker', car.maker)
    #     car.release_year = request.data.get('release_year', car.release_year)
    #     car.vin = request.data.get('vin ', car.vin)
    #     try:
    #         owner = User.objects.get(pk=request.user.pk)
    #         car.owner = owner
    #     except KeyError:
    #         pass        
    #     collection = Collection.objects.get(pk=request.user.pk)
    #     car.collection = collection
    #     serializer = CarSerializer(car, request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
        
    
    
    # @action(detail=True, methods=['Put'])
    # def remove_from_collection(self, request, pk=None, format=None):
    #     car = Car.objects.get(pk=pk)
    #     car.model = request.data.get('model', car.model)
    #     car.maker = request.data.get('maker', car.maker)
    #     car.release_year = request.data.get('release_year', car.release_year)
    #     car.vin = request.data.get('vin ', car.vin)
    #     try:
    #         owner = User.objects.get(pk=request.user.pk)
    #         car.owner = owner
    #     except KeyError:
    #         pass        
    #     collection = Collection.objects.get(pk=request.user.pk)
    #     car.collection = collection
    #     serializer = CarSerializer(car, request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
    

    
#  @action(detail=True, methods=['put'], name='Change Password')
#     def password(self, request, pk=None):
#         """Update the user's password."""
#         ...

#     @password.mapping.delete
#     def delete_password(self, request, pk=None):
#         """Delete the user's password."""
#         ...
        
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
       
       
