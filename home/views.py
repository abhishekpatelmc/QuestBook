from django.shortcuts import render
from home.models import Destination

def index(request):
    dests = Destination.objects.all()
    return render(request, 'home/index.html',{'dests': dests,})