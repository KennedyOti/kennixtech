from django.urls import path
from . import views

# URL Paths that implement routiing

urlpatterns = [
    path('', views.home, name= 'home'),
    
]
