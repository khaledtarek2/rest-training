from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin 
from .models import Car, CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets




        

class CarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving cars.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
    
    
    
# class CarViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving cars.
#     """

#     def list(self, request, format=None):
#         queryset = Car.objects.all()
#         serializer = CarSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None,format=None):
#         queryset = Car.objects.all()
#         car = get_object_or_404(queryset, pk=pk)
#         serializer = CarSerializer(car)
#         return Response(serializer.data)


#     def create(self, request, format=None, **data):
#         queryset = Car.objects.all()
#         serializer = CarSerializer(queryset, **data)
#         return Car.objects.create(serializer.data)
        
        

#     def update(self, request, pk=None, format=None, **data):
#         queryset = Car.objects.all()
#         car = get_object_or_404(queryset, pk=pk)
#         serializer = CarSerializer(car)
#         return Car.objects.update(serializer.data)


