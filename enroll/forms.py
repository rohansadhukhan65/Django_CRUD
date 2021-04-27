from django.core import validators
from django import forms
from .models import User

class StuReg(forms.Form):
    name        = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control '}))
    email       = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control '}))
    passsword = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control '}))
   
