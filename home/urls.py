from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  #library for Django reset password

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/register/', views.register, name='register'),
    path('logout', views.logout, name="logout"),
    path('about', views.about, name='about'),
    path('country_details/<str:country_name>/', views.country_details, name='country_details'),
    path('country_details/<str:country_name>/adventure_details/<str:dest_name>/', views.adventure_details, name='adventure_details'),
    path('adventure_details/<str:dest_name>/', views.adventure_details, name='adventure_details'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='home/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset', views.password_reset_request, name="home/password/password_reset")
]
