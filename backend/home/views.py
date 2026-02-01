from django.shortcuts import render
from .models import Banner

def home(request):
    banners = Banner.objects.filter(is_active=True)
    return render(request, 'home.html', {'banners': banners})
