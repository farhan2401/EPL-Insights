from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

# Create your views here.
def seasons(request):
    ls = seasonsTbl.objects.all()
    return render(request, 'seasons/seasonshome.html', {"ls":ls})

def seasonview(request, usrseason):
    stats = statsTbl.objects.all().filter(season=usrseason)
    return render(request, 'seasons/seasonpage.html', {"stats":stats})