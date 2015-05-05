from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^(?P<relative_url>(.*))/$', 'pages.views.page_detail', name='pages_page_detail')
)
