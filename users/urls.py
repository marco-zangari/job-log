"""Defines url patterns for users."""

from django.urls import path
from django.contrib.auth.views import login

from . import views


app_name = 'users'
url_patterns = [
    path('login/', login, {'template_name': 'users/login.html'}, name='login')
]
