from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# This function renders homepage
def home(request):
    return render(request, 'users/index.html')

