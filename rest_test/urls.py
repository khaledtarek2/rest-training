from django.contrib import admin
from django.urls import path, include
from rest_test.views import CarViewSet, CollectionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'collections', CollectionViewSet, basename='collection')


    
# for url in router.urls:
#     print(url)
    
urlpatterns = [
    path('', include(router.urls))
]


