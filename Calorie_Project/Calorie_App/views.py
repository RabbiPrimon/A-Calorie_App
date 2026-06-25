from django.shortcuts import render, redirect
from Calorie_App.forms import *
from Calorie_App.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register_page(request):

  form_data = RegistrationForm()
  context = {
    'form_data': form_data,
    'form_title': 'User Registration Form',
    'form_btn': 'Register',
  }

  return render (request, 'master/base-form.html',context)