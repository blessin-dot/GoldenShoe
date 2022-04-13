from turtle import title
from django.forms import ModelForm, widgets
from .models import Project
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['shoe_quantity', 'shoe_size']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
