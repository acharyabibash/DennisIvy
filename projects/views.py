from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our products')

def project(request,pk):
    return HttpResponse('SINGLE PROJECT' + ' '+str(pk))