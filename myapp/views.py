from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanyModelSerializer
from rest_framework.response import Response
from rest_framework import status

def StartPage(request):
    return HttpResponse('<p>Hello myapp </p>')

@api_view(['GET'])
def getCompanyList(request):
    try:
        CompanyModelData = Company.objects.all()
        CompanyData = CompanyModelSerializer(CompanyModelData, many=True)
        if (len(CompanyData.data)==0):
            raise Exception('No records found in Database')
        return Response(CompanyData.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error' : str(e)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def getCompanyByID(request, CompanyID):
    print(CompanyID)
    try:
        CompanyModelDataID = Company.objects.filter(CompanyID = CompanyID)
        CompanyData = CompanyModelSerializer(CompanyModelDataID, many=True)
        if len(CompanyData.data)==0:
            raise Exception('Company not found in Database.')
        return Response(CompanyData.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error' : str(e)}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def createNewCompany(request):
    try:
        UserCompanyID = request.data.get('CompanyID')
        UserCompanyName = request.data.get('CompanyName')
        if UserCompanyID=='' or UserCompanyName=='':
            raise Exception('Fill Complete Details')
        Company.objects.create(
            CompanyID = UserCompanyID,
            CompanyName = UserCompanyName
        )
        return Response({'status': 'Company Created in Databae'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def deleteCompanyByID(request):
    try:
        deleteCompanyId = request.data.get('CompanyID')
        company = Company.objects.filter(CompanyID=deleteCompanyId).first()
        if company is None:
            raise Exception('Company Not found in Database')
        company.delete()
        return Response({'status': 'Company Deleted in Database.'}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateCompany(request):
    try:
        UserCompanyID = request.data.get('CompanyID')
        UserCompanyName = request.data.get('CompanyName')
        CompanyObjID = Company.objects.filter(CompanyID = UserCompanyID).first()
        if CompanyObjID is None:
            raise Exception('Company Not found in Database.')
        CompanyObjID.CompanyName = UserCompanyName
        CompanyObjID.save()
        return Response({'status': 'Company Updated in Database.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error' : str(e)}, status=status.HTTP_400_BAD_REQUEST) 
    

def displayNewCompany(request):
    return render(request, 'createCompany.html')

def deletePageView(request):
    return render(request, 'deleteCompany.html')

def updatePageView(request):
    return render(request, 'updateCompany.html')