from django.contrib import admin
from home.models import Destination, Detailed_desc, PassengerDetail

# Register your models here.
admin.site.register(Destination)
admin.site.register(Detailed_desc)
admin.site.register(PassengerDetail)