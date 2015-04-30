from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', include(admin.site.urls)),
]

# if 'rosetta' in settings.INSTALLED_APPS:
#    urlpatterns += [
#        url(r'^rosetta/', include('rosetta.urls')),
#    ]

# UPLOAD MEDIA IN DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
