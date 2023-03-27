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
