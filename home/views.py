from django.shortcuts import render
from home.models import Destination, Detailed_desc

def index(request):
    dests = Destination.objects.all()
    return render(request, 'home/index.html',{'dests': dests,})

def about(request):
    return render(request, 'home/about.html')

def country_details(request,country_name):
    country = Destination.objects.all()
    dests = Detailed_desc.objects.all().filter(country=country_name)
    return render(request,'home/country_details.html',{'dests': dests, 'country':country})

def adventure_details(request,dest_name,country_name):
    country = Destination.objects.all()
    country_name = Destination.objects.get(country=country_name)
    dest = Detailed_desc.objects.get(dest_name=dest_name)
    return render(request,'home/adventure_details.html',{'dest': dest, 'country_name': country_name ,'country':country})