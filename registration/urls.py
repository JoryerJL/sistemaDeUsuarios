from django.urls import path, include
from .views import *

app_name = 'registration'

urlpatterns = [
    path('', index, name='index'),
    path('custom-login/', custom_login, name='custom_login'),
    path('custom-register/', custom_register, name='custom_register'),
    path('logout/', logout_view, name='logout_view'),
    path('custom-change-password/', custom_change_password, name='change_password'),
    path('django-register/', django_register, name='django_register'),
    path('django-login/', django_login, name='django_login'),
]