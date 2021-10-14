from django.urls import path
from .views import home, federalregister, FRList, FRDetail, Subscribe, UserSubscriptions, Subscribers, UserSubscriptionsList, FeedNameList, FeedNameUpdate, addfeed
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', home, name='home'),
    path('federalregister', federalregister, name='federalregister'),
    
    path('frapi/', FRList.as_view()),
    path('frapi/<int:pk>', FRDetail.as_view()),

    path('usersubscriptions/<int:pk>', UserSubscriptions.as_view()),
    path('usersubscriptionslist/', addfeed),

    path('subscriber/', Subscribe.as_view()),
    path('subscribers/<int:pk>', Subscribers.as_view()),

    path('feedlist', FeedNameList.as_view()),
    path('feedlistupdate', FeedNameUpdate.as_view()),
    
]