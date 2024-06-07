from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

# Create your views here.
def teams(request):
    teams = teamsTbl.objects.all()
    return render(request, 'teams/teamshome.html', {"teams":teams})