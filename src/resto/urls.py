from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path 
from content.views import index, about, menu, gallery, blog, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)