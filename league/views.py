

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from lol.lol_rw import lol_summoner


from django.http import HttpResponseRedirect
from .forms import NameForm

def index(request):
    
    s = lol_summoner()
    
    return HttpResponse(s.rank('Dragoon112'))

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})