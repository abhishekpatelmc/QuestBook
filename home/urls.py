from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('destination_list/<str:city_name>/', views.destination_list, name='destination_list'),
    path('destination_details/<str:city_name>/', views.destination_details, name='destination_details'),
]