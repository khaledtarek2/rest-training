from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .filters import CarFilter




        

# class CarViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for listing or retrieving cars.
#     """
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
    
    
    
    
    
class CarViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving cars.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (filters.DjangoFilterBackend)
    filterset_class = CarFilter
    
    def list(self, request, format=None):
        serializer = CarSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None,format=None):
        car = get_object_or_404(self.queryset, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)


    def create(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
        

    def update(self, request, pk=None, format=None):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
       
       


