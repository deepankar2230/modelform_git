from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='path'),
    path('register/',register,name='register')
]
