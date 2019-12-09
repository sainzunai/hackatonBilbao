from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MyForm(forms.Form):
 # Crear un <input> con un label y una restricción de 100 caracteres
 nombre = forms.CharField(label='Introduce tu nombre', max_length=100)
 # Crear un <input> con type=”email”
 email = forms.EmailField(label='Introduce tu email', max_length=20)

class LoginForm(forms.Form):
    Username = forms.CharField(label = 'Username', max_length = 50)
    password = forms.CharField(label= 'Password', max_length = 50)

class CustomUserForm(UserCreationForm):
    pass

    