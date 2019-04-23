#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.contrib import admin
from websocial import views, rssfeed

#urlpatterns = patterns('',
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(?P<user_id>\d+)/timeline/$', views.timeline),
    url(r'^user/(?P<user_id>\d+)/timeline/json/$', views.timeline_json),
    url(r'^user/(?P<user_id>\d+)/$', views.user_statuses),
    url(r'^user/(?P<follower_user_id>\d+)/following/user/(?P<followee_user_id>\d+)/', views.user_following_user),
    url(r'^user/(?P<user_id>\d+)/following/', views.following),
    url(r'^user/(?P<user_id>\d)/status/$', views.user_statuses),
    url(r'^user/(?P<user_id>\d)/status/json/$', views.user_statuses_json),
    url(r'^user/(?P<user_id>\d+)/rss/$', rssfeed.UserStatusRssFeed()),
    url(r'^search/', views.search),
    url(r'^$', views.home),
]
#)
