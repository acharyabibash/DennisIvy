from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project
projectsList = [
    {
        'id':'1',
        'title':"Ecommerce website",
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':"Portfolio website",
        'description':'This was a project where I build out my portfolio'
    },
    {
        'id':'3',
        'title':"Social Network",
        'description':'Awesome open source project I am still working on'
    }
]

def projects(request):
    projects = Project.objects.all()
    context={'projects':projects}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{'project':projectObj})