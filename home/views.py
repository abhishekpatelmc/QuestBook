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
    return render(request, 'home/about.html')


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


# def booking(request):
#     return render(request, 'home/booking.html')


# class KeyValueForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField()
# def pessanger_detail_def(request, city_name):
#     PassengerDetailsForm = formset_factory(pessanger_detail, extra=1)
#     if request.method == 'POST':
#         formset = PassengerDetailsForm(request.POST)
#         if formset.is_valid():
#             if 'trip_date' in request.POST:
#                 temp_date = datetime.strptime(request.POST['trip_date'], "%Y-%m-%d").date()
#             else:
#                 # handle missing trip_date field
#                 return redirect('index')
#             date1 = datetime.now().date()
#             if temp_date < date1:
#                 return redirect('index')
#             obj = pessanger_detail.objects.get(Trip_id=3)
#             pipo_id = obj.Trip_same_id
#             #pipo_id =4
#             request.session['Trip_same_id'] = pipo_id
#             price = request.session['price']
#             city = request.session['city']
#             print(request.POST['trip_date'])
#             #temp_date = parse_date(request.POST['trip_date'])
#             temp_date = datetime.strptime(request.POST['trip_date'], "%Y-%m-%d").date()
#             usernameget = request.user.get_username()
#             print(temp_date)
#             request.session['n']=formset.total_form_count()
#             for i in range(0, formset.total_form_count()):
#                 form = formset.forms[i]
#
#                 t = pessanger_detail(Trip_same_id=pipo_id,first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
#                                      age=form.cleaned_data['age'],
#                                      Trip_date=temp_date,payment=price,username=usernameget,city=city)
#                 t.save()
#                 # print (formset.forms[i].form-[i]-value)
#
#             obj.Trip_same_id = (pipo_id + 1)
#             obj.save()
#             no_of_person = formset.total_form_count()
#             price1 = no_of_person * price
#             GST = price1 * 0.13
#             GST = float("{:.2f}".format(GST))
#             final_total = GST + price1
#             request.session['pay_amount'] = final_total
#             return render(request,'home/payment.html', {'no_of_person': no_of_person,'price1': price1, 'GST': GST, 'final_total': final_total,'city': city })
#     else:
#         formset = PassengerDetailsForm()
#         return render(request, 'home/booking.html', {'formset': formset, 'city_name': city_name, })

def passenger_detail(request, city_name,country_name,dest_name):
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
