from django.urls import path
from predictions import views

urlpatterns = [
    path("", views.predictions, name="predictions"),
    path("Week <int:usrweek>/", views.weekview, name="weekview")
]