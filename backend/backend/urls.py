from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),          # Home
    path('about/', include('about.urls')),   # About
    path('dashboard/', include('dashboard.urls')),  # CMS
    path('accounts/', include('accounts.urls')),    # Login
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
