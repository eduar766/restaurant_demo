from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include 
from content.views import index, about, menu, gallery, contact
from blog.views import search, blog, post, post_delete, post_update, post_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('tinymce/', include('tinymce.urls')),

    path('search/', search, name='search'),

    path('blog/', blog, name='blog'),
    path('create/', post_create, name='create'),
    path('post/<id>/', post, name='post' ),
    path('post/<id>/update', post_update, name='post-update' ),
    path('post/<id>/delete', post_delete, name='post-delete' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)