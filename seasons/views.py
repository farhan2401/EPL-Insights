from django.shortcuts import render
from sqlite3 import *

# Create your views here.
def seasons(request):
    ls = matches.objects.get(id=id)
    return render(request, 'seasons/seasonshome.html', {"ls":ls})