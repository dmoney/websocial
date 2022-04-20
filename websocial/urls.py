#from django.conf.urls import patterns, include, url
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from websocial import views, rssfeed

#urlpatterns = patterns('',
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^user/(?P<user_id>\d+)/timeline/$', views.timeline),
    re_path(r'^user/(?P<user_id>\d+)/timeline/json/$', views.timeline_json),
    re_path(r'^user/(?P<user_id>\d+)/$', views.user_statuses),
    re_path(r'^user/(?P<follower_user_id>\d+)/following/user/(?P<followee_user_id>\d+)/', views.user_following_user),
    re_path(r'^user/(?P<user_id>\d+)/following/', views.following),
    re_path(r'^user/(?P<user_id>\d)/status/$', views.user_statuses),
    re_path(r'^user/(?P<user_id>\d)/status/json/$', views.user_statuses_json),
    re_path(r'^user/(?P<user_id>\d+)/rss/$', rssfeed.UserStatusRssFeed()),
    re_path(r'^search/', views.search),
    re_path(r'^$', views.home),
]
#)
