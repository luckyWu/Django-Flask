from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('create_index/',views.index_create),
    path('index/',views.index),
]
