from django.shortcuts import render

def index(request):
    # dests = Destination.objects.all()
    return render(request, 'home/index.html', )
    # return render(request, 'home/index.html',{'dests': dests})