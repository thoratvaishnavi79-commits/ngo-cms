from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Slider


@login_required
def dashboard_home(request):
    return render(request, 'dashboard/index.html')


@login_required
def manage_slider(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        if title and image:
            Slider.objects.create(title=title, image=image)

        return redirect('dashboard:manage-slider')

    sliders = Slider.objects.all().order_by('-id')

    return render(request, 'dashboard/manage_slider.html', {
        'sliders': sliders
    })


@login_required
def delete_slider(request, slider_id):
    slider = Slider.objects.get(id=slider_id)
    slider.delete()
    return redirect('dashboard:manage-slider')
