from django.urls import path
from predictions import views

urlpatterns = [
    path("", views.predictions, name="predictions"),
]