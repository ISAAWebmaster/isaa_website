from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def isaa_home(request):
    print(request)
    template = loader.get_template('isaa_home.html')
    return HttpResponse(template.render())

def isaa_clubs(request):
    template = loader.get_template('isaa_clubs.html')
    return HttpResponse(template.render())

def isaa_history(request):
    template = loader.get_template('isaa_history.html')
    return HttpResponse(template.render())

def isaa_resources(request):
    template = loader.get_template('isaa_resources.html')
    return HttpResponse(template.render())

def isaa_gallery(request):
    template = loader.get_template('isaa_gallery.html')
    return HttpResponse(template.render())