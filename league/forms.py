'''
Created on 31 Jan 2018

@author: Arnolds
'''
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)