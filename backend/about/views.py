from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OurStory, CoreValue, Program, TeamMember


# =========================
# PUBLIC ABOUT PAGE
# =========================
def about_page(request):
    context = {
        "story": OurStory.objects.first(),
        "core_values": CoreValue.objects.all(),
        "programs": Program.objects.all(),
        "team_members": TeamMember.objects.all(),
    }
    return render(request, "about/about.html", context)


# =========================
# ADMIN DASHBOARD
# =========================
@login_required
def about_dashboard(request):
    story, _ = OurStory.objects.get_or_create(id=1)

    if request.method == 'POST' and 'story_submit' in request.POST:
        story.content = request.POST.get('content')
        story.save()

    context = {
        "story": story,
        "core_values": CoreValue.objects.all(),
        "programs": Program.objects.all(),
        "team_members": TeamMember.objects.all(),
    }

    return render(request, "about/dashboard.html", context)


# =========================
# CORE VALUES
# =========================
@login_required
def add_core_value(request):
    if request.method == 'POST':
        CoreValue.objects.create(value=request.POST.get('value'))
    return redirect('about-dashboard')


@login_required
def delete_core_value(request, id):
    CoreValue.objects.get(id=id).delete()
    return redirect('about-dashboard')


# =========================
# PROGRAMS
# =========================
@login_required
def add_program(request):
    if request.method == 'POST':
        Program.objects.create(title=request.POST.get('title'))
    return redirect('about-dashboard')


@login_required
def delete_program(request, id):
    Program.objects.get(id=id).delete()
    return redirect('about-dashboard')


# =========================
# TEAM MEMBERS
# =========================
@login_required
def add_team_member(request):
    if request.method == 'POST':
        TeamMember.objects.create(
            name=request.POST.get('name'),
            role=request.POST.get('role'),
            image=request.FILES.get('image')
        )
    return redirect('about-dashboard')


@login_required
def delete_team_member(request, id):
    TeamMember.objects.get(id=id).delete()
    return redirect('about-dashboard')
from django.shortcuts import get_object_or_404
from .models import Program

def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)
    return render(request, "about/program_detail.html", {
        "program": program
    })
