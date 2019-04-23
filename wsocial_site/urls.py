from django.conf.urls import patterns, include, url
from django.contrib import admin
import websocial.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wsocial_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(websocial.urls)),
)
