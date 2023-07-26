from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def Dashboards(request):
    template=loader.get_template('myApp/Dashboards.html')
    return HttpResponse(template.render({},request))

def stories(request):
    template=loader.get_template('myApp/stories.html')
    return HttpResponse(template.render({},request))

def about(request):
    template = loader.get_template('myApp/aboutproject.html')
    return HttpResponse(template.render({},request))

def profile(request):
    template=loader.get_template('myApp/profile.html')
    return HttpResponse(template.render({},request))
