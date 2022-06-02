from django.urls import path

from .views import *

urlpatterns = [
    path('init/', init, name='ex00-init')
]