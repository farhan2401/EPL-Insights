from django.shortcuts import render
from django.http import HttpResponse
from predictions.models import *
from predictions.poisson import *

# Create your views here.
def predictions(request):
    wk1 = upcomingPreds.objects.filter(week=1)
    return render(request, 'predictions/predictions.html', {'wk1': wk1})

def weekview(request, usrweek):
    weekPreds = upcomingPreds.objects.filter(week=usrweek)
    return render(request, 'predictions/weekpage.html', {'weekPreds': weekPreds})