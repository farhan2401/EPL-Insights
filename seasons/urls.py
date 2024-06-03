from django.urls import path
from seasons import views
    
urlpatterns = [
    path("", views.seasons, name="seasons"),
    path("seasonview/", views.seasonview, name="seasonview")
]