from django.urls import path
from .views import *

app_name = 'registration'

urlpatterns = [
    path('', index, name='index'),
    path('custom-login/', custom_login, name='custom_login'),
]