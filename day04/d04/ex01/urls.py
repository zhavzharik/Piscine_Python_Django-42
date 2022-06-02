from django.urls import path

from .views import *

urlpatterns = [
    path('django/', django),
    path('display/', display),
    path('templates/', templates)
]