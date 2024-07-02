from django.shortcuts import render
from django.http import HttpResponse
from predictions.models import *
from predictions.poisson import *

# Create your views here.
def predictions(request):
    results = upcomingPreds.objects.all()
    print(results)
    return render(request, 'predictions/predictions.html', {"results":results})