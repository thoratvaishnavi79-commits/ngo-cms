from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')
