from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('country_details/<str:city_name>/', views.country_details, name='country_details'),
    # path(country_details/adventure_details/<str:city_name>', views.destination_details, name='adventure_details'),
]