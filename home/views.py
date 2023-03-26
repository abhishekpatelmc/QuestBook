from django.shortcuts import render
from home.models import Destination, Detailed_desc

def index(request):
    dests = Destination.objects.all()
    return render(request, 'home/index.html',{'dests': dests,})

def about(request):
    return render(request, 'home/about.html')

def country_details(request,city_name):
    country = Destination.objects.all()
    dests = Detailed_desc.objects.all().filter(country=city_name)
    return render(request,'home/country_details.html',{'dests': dests, 'country':country})

def adventure_details(request,dest_name):
    country = Destination.objects.all()
    dest = Detailed_desc.objects.get(dest_name=dest_name)
    price = dest.price
    return render(request,'home/adventure_details.html',{'dest': dest, 'country':country, 'price':price})