from django.urls import path
from . import views
app_name = 'about'
urlpatterns = [
    path('', views.about_page, name='about'),
    path('dashboard/', views.about_dashboard, name='about-dashboard'),

    path('add-core-value/', views.add_core_value, name='add-core'),
    path('delete-core-value/<int:id>/', views.delete_core_value, name='delete-core'),

    path('add-program/', views.add_program, name='add-program'),
    path('delete-program/<int:id>/', views.delete_program, name='delete-program'),

    path('add-team/', views.add_team_member, name='add-team'),
    path('delete-team/<int:id>/', views.delete_team_member, name='delete-team'),
    path('program/<slug:slug>/', views.program_detail, name='program-detail'),
 path('', views.about_page, name='about'),
    path('dashboard/', views.about_dashboard, name='dashboard'),
]
