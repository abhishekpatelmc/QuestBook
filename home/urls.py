from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/register/', views.register, name='register'),
    path('about', views.about, name='about'),
    path('country_details/<str:country_name>/', views.country_details, name='country_details'),
    path('country_details/<str:country_name>/adventure_details/<str:dest_name>/', views.adventure_details,name='adventure_details'),
    path('adventure_details/<str:dest_name>/', views.adventure_details, name='adventure_details'),
    path('booking', views.passenger_detail, name='booking'),
    path('country_details/<str:country_name>/adventure_details/<str:city_name>/passenger_detail/<str:dest_name>', views.passenger_detail, name='passenger_detail'),
    path('adventure_details/<str:dest_name>/passenger_detail/<str:city_name>', views.passenger_detail,name='passenger_detail'),
    re_path(r'^.*/$', RedirectView.as_view(url='/about', permanent=False), name='about_any'),
]