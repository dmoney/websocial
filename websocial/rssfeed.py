from django.contrib.syndication.views import FeedDoesNotExist
from django.shortcuts import get_object_or_404
from websocial.models import User, Status
from django.contrib.syndication.views import Feed

class UserStatusRssFeed(Feed):
    def get_object(self, request, user_id):
        return get_object_or_404(User, pk=user_id)

    def title(self, obj):
        return "Statuses for %s" % obj
    
    def link(self, obj):
        return obj.get_absolute_url()
    
    def description(self, obj):
        return "Statuses for %s" % obj
    
    def items(self, obj):
        return obj.status_set.all()[:100]
