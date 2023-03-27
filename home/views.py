from home.models import Destination, Detailed_desc
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect


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
    dest = Detailed_desc.objects.get(dest_name=dest_name)
    return render(request,'home/adventure_details.html',{'dest': dest,'country':country})

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
            content = 'Hello ' + request.user.first_name + ' ' + request.user.last_name + '\n' + ', You are logged in to our site. Stay connected and keep travelling.'
            dests = Destination.objects.all()
            return render(request, 'home/index.html',{'dests':dests})
        else:
            messages.info(request, 'Invalid credential')
            return redirect('login')
    else:
        return render(request, 'home/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

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
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, last_name=last_name,
                                                first_name=first_name)
                user.save()
                print('user Created')
                return redirect('home/login')
        else:
            messages.info(request, 'password is not matching ')
            return redirect('register')
    else:
        return render(request, 'home/register.html')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "password Reset Requested"
					email_template_name = "home/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("index")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="home/password/password_reset.html", context={"password_reset_form":password_reset_form})
