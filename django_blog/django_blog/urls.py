from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^sobre$', 'blog.views.sobre', name='sobre'),
    url(r'^interna/(?P<slug>[0-9A-Za-z\-_]+)$',
        'blog.views.interna', name='interna'),
    url(r'^formulario$', 'django_media_center.views.upload_img', name='form'),
    url(r'^listagem/(?P<category>[0-9A-Za-z]+)$', 'blog.views.listagem', name='listagem'),
    url(r'^listagem_geral$', 'blog.views.listagem_geral', name='listagem_geral'),
    url(r'^hashtags$', 'blog.views.hashtags', name='hashtags'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

