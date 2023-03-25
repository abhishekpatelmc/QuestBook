from django.shortcuts import render
from home.models import Destination, Detailed_desc

def index(request):
    dests = Destination.objects.all()
    return render(request, 'home/index.html',{'dests': dests,})

def destination_list(request,city_name):
    dests = Detailed_desc.objects.all().filter(country=city_name)
    return render(request,'home/country_details.html',{'dests': dests})

def destination_details(request,city_name):
    dest = Detailed_desc.objects.get(dest_name=city_name)
    price = dest.price
    request.session['price'] = price
    request.session['city'] = city_name
    return render(request,'home/adventure_details.html',{'dest':dest})