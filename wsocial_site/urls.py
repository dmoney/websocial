from django.conf.urls import patterns, include
from django.urls import re_path
from django.contrib import admin
import websocial.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wsocial_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^', include(websocial.urls)),
)
