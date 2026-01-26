from django.shortcuts import render
from .models import Banner

def homepage(request):
    banners = Banner.objects.all()
    return render(request, 'home.html', {'banners': banners})
