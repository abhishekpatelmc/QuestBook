from django.shortcuts import render
from home.models import Destination, Detailed_desc, PassengerDetail
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import PassengerDetailsForm
from django import forms
from django.forms.formsets import formset_factory
from datetime import datetime
from django.contrib.auth.models import User


def index(request):
    dests = Destination.objects.all()
    adventures = Detailed_desc.objects.all()[:6]
    return render(request, 'home/index.html', {'dests': dests, 'adventures': adventures})


def about(request):
    country = Destination.objects.all()
    return render(request, 'home/about.html',{'country': country})


def country_details(request, country_name):
    country = Destination.objects.all()
    country_details = Destination.objects.get(country=country_name)
    dests = Detailed_desc.objects.all().filter(country=country_name)
    return render(request, 'home/country_details.html', {'dests': dests, 'country': country, 'country_name': country_name, 'country_details': country_details})


def adventure_details(request, dest_name, country_name=None):
    country = Destination.objects.all()
    dest = Detailed_desc.objects.get(dest_name=dest_name)
    return render(request, 'home/adventure_details.html', {'dest': dest, 'country': country})


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
            dests = Destination.objects.all()
            return render(request, 'home/index.html', {'dests': dests})
        else:
            messages.info(request, 'Invalid credential')
            return redirect('login')
    else:
        return render(request, 'home/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, last_name=last_name,
                                                first_name=first_name)
                user.save()
                print('user Created')
                return redirect('home/login.html')
        else:
            messages.info(request, 'Password is not matching ')
            return redirect('home/login/register.html')
        return redirect('index.html')
    else:
        return render(request, 'home/register.html')


def passenger_detail(request,city_name,country_name=None,dest_name=None):
    msg = ""
    if request.method == "POST":
        form = PassengerDetailsForm(request.POST)
        if form.is_valid():
            booking_data = form.save(commit=False)
            booking_data.save()
            msg = 'Your order has been placed successfully.'
        else:
            msg = 'We do not have sufficient stock to fill your order.'
        return render(request, 'home/payment.html', {'msg': msg})
    else:
        form = PassengerDetailsForm()
    return render(request, 'home/booking.html', {'form': form, 'msg': msg})
