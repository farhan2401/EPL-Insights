from django.shortcuts import render
from home.models import currTbl

# Create your views here.
def home(request):
    standings = currTbl.objects.all()
    return render(request, 'home/homepage.html', {"standings": standings})