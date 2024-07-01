from django.shortcuts import render
from django.http import HttpResponse
from predictions.models import upcomingMatches

# Create your views here.
def predictions(request):
    return render(request, 'predictions/predictions.html', {})