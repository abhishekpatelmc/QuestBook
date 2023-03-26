from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('country_details/<str:city_name>/', views.country_details, name='country_details'),
    path('adventure_details/<str:dest_name>/', views.adventure_details, name='adventure_details'),
    path('country_details/Australia/adventure_details/<str:dest_name>', views.adventure_details, name='adventure_details'),
]