from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

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
    page = 'projects'
    number = 10
    context={'page':page,'number':number,'projects':projectsList}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request,'projects/single-project.html',{'project':projectObj})