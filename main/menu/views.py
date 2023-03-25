from django.shortcuts import render
from menu.models import Menu, MenuItem
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'menu/index.html')    
