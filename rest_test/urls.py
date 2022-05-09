from django.contrib import admin
from django.urls import path, include
from rest_test.views import CarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', CarViewSet, 'car')


for url in router.urls:
    print(url, '\n')
    
    
    
urlpatterns = [
    path('', include(router.urls)), 
]


