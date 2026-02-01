from django.urls import path
from .views import admin_login
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', admin_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
]
