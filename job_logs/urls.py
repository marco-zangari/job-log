"""Define URL patterns for job_logs."""


from django.urls import path
from . import views

app_name = 'job_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
]
