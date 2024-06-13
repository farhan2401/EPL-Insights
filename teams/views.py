from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

# Create your views here.
def teams(request):
    teams = teamsTbl.objects.all()
    return render(request, 'teams/teamshome.html', {"teams":teams})

def teamview(request, usrteam):
    stats = statsTbl.objects.all().filter(squad=usrteam)
    context = {"stats": stats}
    return render(request, 'teams/teampage.html', context)

def teammatchview(request, usrteam, usrseason):
    home = matchesTbl.objects.all().filter(home=usrteam).filter(season=usrseason)
    away = matchesTbl.objects.all().filter(away=usrteam).filter(season=usrseason)
    context = {"home": home, "away": away}
    return HttpResponse("Matches")