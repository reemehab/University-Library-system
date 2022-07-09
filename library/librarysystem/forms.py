from django import forms
from django.db.models import fields
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields= '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=[
            'username',
            'birthDate',
             'address',
             'city',
             'email',
             'password',

 
            
        ]

