# from dataclasses import fields
from eshop.models import *
from django import forms
# from django.contrib.auth.forms import UserCreationForm

class SignUpForm(forms.ModelForm):
    # username = forms.CharField(label='email', min_length=5, max_length=150)  
    password = forms.CharField(widget=forms.PasswordInput, label=('password'))
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","email","password")
        # labels = {'username': 'email'}
        # Widget= {
        #     'username': 'email'
        # }