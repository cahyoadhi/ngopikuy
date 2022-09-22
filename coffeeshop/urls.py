from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ngopikuy.urls")),
    path('unicorn/', include("django_unicorn.urls")),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
]

handler404 = 'ngopikuy.views.page_not_found'
