from django.urls import path
from .views import home, federalregister
from django.conf.urls import url




urlpatterns = [
    path('', home, name='home'),
    path('federalregister', federalregister, name='federalregister'),
    
]