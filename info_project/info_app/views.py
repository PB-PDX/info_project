from django.shortcuts import redirect, render
import requests
from .models import FederalRegister
from django.http.response import JsonResponse

import xmltodict

from django.shortcuts import render
from django.http import HttpResponse

import json


def home(request):
    return render(request, 'info_app/home.html')


def federalregister(request):
    data= requests.get('http://www.federalregister.gov/api/v1/documents.rss?&amp;conditions%5Bagency_ids%5D%5B%5D=466&amp;order=newest')
    response = data.text
    dict_data = xmltodict.parse(response)
    json_data = json.dumps(dict_data, indent=3)
    x= json.loads(json_data)
    snips = x['rss']['channel']['item']
    
    return render(request, 'info_app/federalregister.html', {'snips' : snips})

