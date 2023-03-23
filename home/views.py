from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from home.models import Country, Adeventure

# Create your views here.
def index(request):
    countries = Country.objects.all()
    return render(request, 'home/index.html', {'countries': countries})

def CountryDetail(request):
    countries = Country.objects.all()
    return render(request, 'home/countrydetail.html', {'countries': countries})

def Adeventure(request):
    adventure = Adeventure.objects.all()
    return render(request, 'home/adventure.html', {'adventure': adventure})

def AdeventureDetail(request):
    adventure = Adeventure.objects.all()
    return render(request, 'home/adventuredetail.html', {'adventure': adventure})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Sucessfully Logged in')
            email = request.user.email
            print(email)
            content = 'Hello ' + request.user.first_name + ' ' + request.user.last_name + '\n' + 'You are logged in in our site.keep connected and keep travelling.'
            # send_mail('Alert for Login', content
            #           , 'travellotours89@gmail.com', [email], fail_silently=True)
            # dests = Destination.objects.all()
            # return render(request, 'index.html',{'dests':dests})
        else:
            messages.info(request, 'Invalid credential')
            return redirect('login')
    else:
        return render(request, 'login.html')