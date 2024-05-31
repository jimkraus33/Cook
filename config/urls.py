from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import settings


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('theboss/', admin.site.urls),
    path('', include('recipes.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
