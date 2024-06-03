from django.shortcuts import render
from django.http import HttpResponse
from home.models import seasonsTbl

# Create your views here.
def seasons(request):
    ls = seasonsTbl.objects.all()
    return render(request, 'seasons/seasonshome.html', {"ls":ls})

def seasonpage(request):
    return render(request, 'seasons/seasonpage.html', {})