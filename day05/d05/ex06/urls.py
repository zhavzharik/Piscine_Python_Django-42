from django.urls import path

from .views import *

urlpatterns = [
    path('init/', Init.as_view(), name='ex06-init'),
    path('populate/', Populate.as_view(), name='ex06-populate'),
    path('display/', Display.as_view(), name='ex06-display'),
    path('remove/', Remove.as_view(), name='ex06-remove'),
    path('update/', Update.as_view(), name='ex06-update')
]