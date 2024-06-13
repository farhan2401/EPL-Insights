from django.urls import path
from teams import views
    
urlpatterns = [
    path("", views.teams, name="teams"),
    path("<str:usrteam>/", views.teamview, name="teamview"),
    path("<str:usrteam>/<str:usrseason>", views.teammatchview, name="teammatchview")
]