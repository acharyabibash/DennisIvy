from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def projects(request):
    page = 'projects'
    number = 10
    context={'page':page,'number':number}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    return render(request,'projects/single-project.html')