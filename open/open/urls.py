from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from short_url.views import URLCreateView, URLListView

urlpatterns = patterns('',
    url(r'^result/$', URLListView.as_view(), name = 'result'),
    #url(r'^result/$', TemplateView.as_view(template_name='short_url/result.html', name = 'result'),
    url(r'^$', URLCreateView.as_view(), name = 'create'),
    #url(r'^result/$', Result.as_view(), name = 'result'),
    # Examples:
    # url(r'^$', 'open.views.home', name='home'),
    # url(r'^open/', include('open.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
