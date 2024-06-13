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
    homeGames = matchesTbl.objects.all().filter(home=usrteam).filter(season=usrseason)
    awayGames = matchesTbl.objects.all().filter(away=usrteam).filter(season=usrseason)
    context = {"homeGames": homeGames, "awayGames": awayGames}
    if usrseason == "2017-2018":
        return render(request, 'teams/20172018page.html', context)
    elif int(usrseason[:4]) > 2017:
        return render(request, 'teams/nomissingdata.html', context)
    elif int(usrseason[:4]) < 2017 and int(usrseason[:4]) > 1991:
        return render(request, 'teams/2016-1992.html', context)
    else:
        return render(request, 'teams/1991end.html', context)