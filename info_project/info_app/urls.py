from django.urls import path
from .views import home, federalregister, FRList, FRDetail, Subscribe, SnipSubscribe, Subscribers
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', home, name='home'),
    path('federalregister', federalregister, name='federalregister'),
    
    path('frapi/', FRList.as_view()),
    path('frapi/<int:pk>', FRDetail.as_view()),
    path('subscriber/', Subscribe.as_view()),
    path('subscribersnip/<int:pk>', SnipSubscribe.as_view()),
    path('subscribers/<int:pk>', Subscribers.as_view()),
    
]