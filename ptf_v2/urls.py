from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Projects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Projects.views.home, name='home'),
    path('projects/', include('Projects.urls')),
    path('code/', include('Code.urls')),
    path('presentations/', include('Presentations.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

