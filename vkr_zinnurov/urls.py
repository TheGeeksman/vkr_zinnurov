from django.contrib import admin
from django.urls import path, include

from vkr_zinnurov import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('deffect_detect.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )