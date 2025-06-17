from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanyModelSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def StartPage(request):
    return HttpResponse('<p>Hello myapp </p>')

@api_view(['GET'])
def getCompanyList(request):
    try:
        CompanyModelData = Company.objects.all()
        print('LENGTH:   ', CompanyModelData)
        CompanyData = CompanyModelSerializer(CompanyModelData, many=True)
        return Response(CompanyData.data, status=status.HTTP_200_OK)
    except:
        return Response({'error' : 'Retrieve Failed'}, status=status.HTTP_404_NOT_FOUND)