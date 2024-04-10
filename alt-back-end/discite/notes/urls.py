from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'mdeditor/', include('mdeditor.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)