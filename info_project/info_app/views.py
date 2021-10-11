from django.shortcuts import redirect, render
import json
import requests
from .models import FederalRegister
import xmltodict
from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone
from users.models import Profile
#-----------------------------------------------------
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import ProfileSerializer
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics 


@api_view(["GET", "POST"])
def addfeed(request, format=None):
    if request.method == 'GET':
        feed = Profile.objects.all()
        serializer = ProfileSerializer(feed, many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE',])
def feed_detail(request, pk):
    try: 
        tutorial = Profile.objects.get(pk=pk) 
    except Profile.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = ProfileSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = ProfileSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

def home(request):
    x = FederalRegister.objects.all()
    return render(request, 'info_app/home.html')






class FRList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FRDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer






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
            # print(pubDate)
            # print(description)
            # pubDate = snip['pubDate'].split(",", 1)
            
            # date_time_str = x
            # print(date_time_str)
            # date_time_obj = datetime.strptime(date_time_str,'%Y-%m-%d')
            # print(date_time_obj)
            link = snip['link']
            data = FederalRegister(
                title=title,
                description=description,
                pubDate=pubDate,
                link=link,
            )
            data.save()
        except:
            print('unable to copy duplicate')
    print(FederalRegister.objects.get(pk=4))
    contact_list = FederalRegister.objects.all()
    paginator = Paginator(contact_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'info_app/federalregister.html', {'page_obj': page_obj})

