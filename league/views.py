

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Summoners
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import dj_pagination as pg


def index(request):
    latest_summoners = Summoners.objects.order_by('-modify_date')[:30]
    template = loader.get_template('league/index.html')
    output = ', '.join([s.name for s in latest_summoners])
    #s = lol_summoner(path = 'lol/')
    ''''
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_summoners, 2)
    
    
    
    try:
        summoners = paginator.page(page)
    except PageNotAnInteger:
        summoners = paginator.page(1)
    except EmptyPage:
        summoners = paginator.page(paginator.num_pages)
    '''
    summoners = latest_summoners
    #sprint(summoners)
    return render(request, 'league/index.html', {'summoners':summoners})



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