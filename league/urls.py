'''
Created on 24 Jan 2018

@author: Arnolds
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]