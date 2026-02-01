from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard:dashboard')

        return render(request, 'accounts/login.html', {
            'error': 'Invalid credentials or not authorized'
        })

    return render(request, 'accounts/login.html')
