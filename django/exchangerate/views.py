from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import requests
# Create your views here.

from datetime import datetime

@api_view(['GET'])
def get_data(request):
    today = datetime.today().strftime("%Y%m%d")
    today = str(int(today) -1)
    api = settings.EXCHANGE_API_KEY
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api}&searchdate={today}&data=AP01'
    response = requests.get(url).json()
    
    return Response({'data':response})

