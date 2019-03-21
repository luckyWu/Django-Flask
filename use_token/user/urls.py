

from django.urls import path, include

from user import views

urlpatterns = [
    path('login/', views.login),
    path('test/', views.test),
    path('userToken/', views.userToken),

]