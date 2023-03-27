from django import forms
from .models import Destination, Detailed_desc, PassengerDetail


class PassengerDetailsForm(forms.ModelForm):
    class Meta:
        model = PassengerDetail
        fields = [
            'first_name',
            'last_name',
            'trip_date',
            'city',
            'payment_currency',

        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'trip_date': 'Trip Date',
            'city': 'City',
            'payment_currency': 'Payment Currency',
        }

class RegisterForm(forms.Form):
    class Meta:
        Model = PassengerDetail
        Fields = [
            'first_name',
            'last_name',
            'password',
            'email',
            'phone',
            
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password': 'Password',
            'email': 'Email',
            'phone': 'Phone Number',
        }