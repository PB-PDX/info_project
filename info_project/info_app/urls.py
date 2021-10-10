from django.urls import path
from .views import home, federalregister, addfeed, feed_detail, FRList, FRDetail
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', home, name='home'),
    path('federalregister', federalregister, name='federalregister'),
    path('api/feed/', addfeed), 
    path('api/feed/<int:pk>', feed_detail),
    path('frapi/', FRList.as_view()),
    path('frapi/<int:pk>', FRDetail.as_view())
    
]