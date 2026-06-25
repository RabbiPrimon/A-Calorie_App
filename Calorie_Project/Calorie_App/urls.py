from django.urls import path
from Calorie_App.views import *

urlpatterns = [
    path('', register_page, name='register_page'),
]