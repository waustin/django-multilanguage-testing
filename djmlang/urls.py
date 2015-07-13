from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView

from filebrowser.sites import site

urlpatterns = [
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^pages/', include('pages.urls')),

    # Filebrowser, DJ Admin, & Grappelli
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
]

# This allows / forces language code to the beginging of these page ursl
# urlpatterns += i18n_patterns(
#    url(r'^pages/', include('pages.urls')),
#)


# UPLOAD MEDIA IN DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
