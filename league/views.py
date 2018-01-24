

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from lol.lol_rw import lol_summoner

def index(request):
    
    s = lol_summoner()
    s.name = "Dragoon112"
    
    return HttpResponse(s.rank())