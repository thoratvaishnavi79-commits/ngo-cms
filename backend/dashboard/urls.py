from django.urls import path
from .views import dashboard_home, manage_slider, delete_slider

urlpatterns = [
    path('', dashboard_home, name='dashboard'),
    path('slider/', manage_slider, name='manage-slider'),
    path('slider/delete/<int:slider_id>/', delete_slider, name='delete-slider'),
]
