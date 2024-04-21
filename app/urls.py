from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #Incluindo todas as urls dos arquivos urls.py(versao 1) de cada app
    path('api/v1/', include('ebooks.urls')),
    path('api/v1/', include('authentication.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)