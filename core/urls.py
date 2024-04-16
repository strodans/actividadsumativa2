from django.contrib import admin
from django.urls import path
from .views import login_usuario,home

urlpatterns = [
    path('', login_usuario,name="login_usuario"),
    path('home',home,name="home"),
]