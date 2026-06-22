from django import forms
from Calorie_App.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationFrom


class RegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    