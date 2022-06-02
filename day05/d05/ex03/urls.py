from django.urls import path

from .views import *

urlpatterns = [
    path('populate/', populate, name='ex03-populate'),
    path('display/', display, name='ex03-display')
]