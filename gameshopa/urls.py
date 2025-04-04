from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.sitemaps.views import sitemap
from .views import StaticViewSitemap
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

sitemaps = {
    'static': StaticViewSitemap,
}

admin.site.site_header = "GAMESHOPA ADMIN"
admin.site.site_title = "Gameshopa Admin Portal"
admin.site.index_title = "Welcome to Gameshopa Admin Portal"

urlpatterns = [
    path('gameshopa-admin-portal/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt")))
]

if settings:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.handler404
handler500 = views.handler500
