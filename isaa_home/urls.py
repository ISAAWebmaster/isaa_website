from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.isaa_home, name='isaa_home'),
    path('home/', views.isaa_home, name='isaa_home'),
    path('clubs/', views.isaa_clubs, name='isaa_club'),
    path('history/', views.isaa_history, name='isaa_history'),
    path('resources/', views.isaa_resources, name='isaa_resources'),
    path('gallery/', views.isaa_gallery, name='isaa_gallery'),
]