from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
# from django.views.static import serve 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ngopikuy.urls")),
    path('unicorn/', include("django_unicorn.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ngopikuy.views.page_not_found'
