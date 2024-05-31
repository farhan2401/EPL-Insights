from django.urls import path
from home import views

urlpatterns = [
    path("stats/", views.home, name="home"),
]