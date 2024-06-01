from django.urls import path
from seasons import views
    
urlpatterns = [
    path("seasons/", views.seasons, name="seasons"),
]