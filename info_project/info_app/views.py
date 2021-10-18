from django.shortcuts import redirect, render
import json

from requests.api import request

import requests
from info_app.models import Feeds, UserSubscriptions, FeedName
import xmltodict
from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone
from users.models import Profile
from django.db.models import Q
from django.views.generic import (
    ListView,
)
#-----------------------------------------------------
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics 
from .serializers import (
    FeedSerializer, 
    UserSubscriptionsSerializer, 
    ProfileSerializer,  
    FeedNameSerializer, 
    ProfileSnipListSerializer,
    )

class SearchResultsView(ListView):
    paginate_by = 10
    model = Feeds
    template_name = 'info_app/search_results.html'
    context_object_name = 'snips'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Feeds.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) 
        )
        object_list = object_list.order_by('-pubDate')
        return object_list

from django.http import HttpResponse
 
def test(request):
    snips = Feeds.objects.filter(subscriber__id=1)
    for snip in snips:
        print(snip.pubDate)
    print(snips)
    return HttpResponse(request, "confirm")





#Profile snippet listview
@api_view(["GET", "PATCH"])
def profilesniplist(request):  
    if request.method == 'GET':
        usersnips = Feeds.objects.filter(subscriber__id=1)

        serializer = ProfileSnipListSerializer(usersnips, many=True)
        
        return Response (serializer.data)
    elif request.method == 'PATCH':
        serializer = UserSubscriptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response ("user exists")

@api_view(["GET", "POST"])
def addfeedsubs(request, format=None):
    if request.method == 'GET':
        user_subscriptions = UserSubscriptions.objects.all()
        serializer = UserSubscriptionsSerializer(user_subscriptions, many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = UserSubscriptionsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response ("user exists")

# @api_view(['GET', 'PUT', 'DELETE',])
# def feed_detail(request, pk):
#     try: 
#         tutorial = Profile.objects.get(pk=pk) 
#     except Profile.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         tutorial_serializer = ProfileSerializer(tutorial) 
#         return JsonResponse(tutorial_serializer.data) 
 
#     elif request.method == 'PUT': 
#         tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = ProfileSerializer(tutorial, data=tutorial_data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# Home page rendering 
def home(request):
    x = Feeds.objects.all()
    return render(request, 'info_app/home.html')

# Listview and create feeds
class Subscribe(generics.ListCreateAPIView):
    queryset = Feeds.objects.all()
    serializer_class = FeedSerializer

class Subscribers(generics.RetrieveUpdateAPIView):
    queryset = Feeds.objects.all()
    serializer_class = FeedSerializer



#Feed update subscriptions for UserSubscriptions model.
class UserSubscriptions(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSubscriptions.objects.all()
    serializer_class = UserSubscriptionsSerializer

class FeedNameUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedName.objects.all()
    serializer_class = UserSubscriptionsSerializer

class FeedNameList(generics.ListCreateAPIView):
    queryset = FeedName.objects.all()
    serializer_class = FeedNameSerializer


class FRList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FRDetail(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer








#api to get xml data and convert it.
def federalregister(request):
    data= requests.get('http://www.federalregister.gov/api/v1/documents.rss?&amp;conditions%5Bagency_ids%5D%5B%5D=466&amp;order=newest')
    response = data.text
    dict_data = xmltodict.parse(response)
    json_data = json.dumps(dict_data, indent=3)
    x= json.loads(json_data)
    results = x['rss']['channel']['item']
    
    for snip in results:
        try:
            title = snip['title']
            
            description = snip['description']
            Date = snip['pubDate'].split(',')[1]
            Date1 = Date.split(' ')
            
            month_name = Date1[2]
            datetime_object = datetime.strptime(month_name, "%b")
            month_number = datetime_object.month
            
            pubDate = Date1[3]+'-'+str(month_number)+'-'+Date1[1]
         
            link = snip['link']
            data = Feeds(
                title=title,
                description=description,
                pubDate=pubDate,
                link=link,
                feed = 'federalregister',
            )
            data.save()
        except:
            print('unable to copy duplicate')
    
    contact_list = Feeds.objects.all()
    paginator = Paginator(contact_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'info_app/federalregister.html', {'page_obj': page_obj})

