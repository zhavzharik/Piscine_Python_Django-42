from django.urls import path

from .views import *

urlpatterns = [
    path('populate/', Populate.as_view(), name='ex05-populate'),
    path('display/', Display.as_view(), name='ex05-display'),
    path('remove/', Remove.as_view(), name='ex05-remove')
]