from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    home, 
    federalregister,
    addfeed, 
    FRList, 
    FRDetail, 
    Subscribe, 
    UserSubscriptions, 
    Subscribers,  
    FeedNameList, 
    FeedNameUpdate,
    SearchResultsView 
)

urlpatterns = [
    #home path
    path('', home, name='home'),

    #POST a new user subscription or return a 404 to initiate an update.
    path('create/subscriptions', addfeed, name='createsubscriptions'),

    #user subscription updates
    path('usersubscriptions/<int:pk>', UserSubscriptions.as_view()),
    
    
    path('subscribers/<int:pk>', Subscribers.as_view()),

    #list of all the feeds and details
    path('feed/list/', Subscribe.as_view()),
    
    #api to get data for the federal register, filtered for SEC
    path('federalregister', federalregister, name='federalregister'),
    
    #Profile views
    path('frapi/', FRList.as_view()),
    path('frapi/<int:pk>', FRDetail.as_view()),
    


    path('feedlist', FeedNameList.as_view()),
    path('feedlistupdate', FeedNameUpdate.as_view()),

    path('search/', SearchResultsView.as_view(), name='search_results'),
    
]