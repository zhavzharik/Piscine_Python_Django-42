from django.urls import path

from .views import *

urlpatterns = [
    path('init/', Init.as_view(), name='ex4-populate'),
    path('populate/', Populate.as_view(), name='ex04-populate'),
    path('display/', Display.as_view(), name='ex04-display'),
    path('remove/', Remove.as_view(), name='ex04-remove')
]