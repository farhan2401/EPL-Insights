from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

# Create your views here.
def teams(request):
    teams = teamsTbl.objects.all()
    return render(request, 'teams/teamshome.html', {"teams":teams})

def teamview(request, usrteam):
    stats = statsTbl.objects.all().filter(squad=usrteam)
    # MAKE IT SO BOTH HOME AND AWAY GAMES ARE DISPLAYED
    matches = matchesTbl.objects.all().filter(home=usrteam).filter(away=usrteam)
    context = {"stats": stats, "matches": matches}
    return render(request, 'teams/teampage.html', context)