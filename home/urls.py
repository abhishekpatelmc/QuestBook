from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/register/', views.register, name='register'),
    path('about', views.about, name='about'),
    path('country_details/<str:country_name>/', views.country_details, name='country_details'),
    path('country_details/<str:country_name>/adventure_details/<str:dest_name>/', views.adventure_details, name='adventure_details'),
    path('adventure_details/<str:dest_name>/', views.adventure_details, name='adventure_details'),
    
]