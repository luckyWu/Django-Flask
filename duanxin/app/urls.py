from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('register/',views.register),
    path('send/',views.send),
    path('res/',views.res),
    path('graph/',views.graph)
]
