from django.urls import path
from seasons import views
    
urlpatterns = [
    path("", views.seasons, name="seasons"),
    path("<str:usrseason>/", views.seasonview, name="seasonview")
]