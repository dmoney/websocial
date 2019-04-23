import feedparser

import sys, time
from os.path import dirname
parent_dir = dirname(dirname(__file__))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'wsocial_site.settings'
from django import setup
setup()
from websocial.models import User, Status
from datetime import datetime

#dking_rss = 'http://dking.org/blog/feed/'
def fetch():
    for user in User.objects.filter(remote=True):
        try:
            feed = feedparser.parse(user.url)
            if feed.get('feed', None) and feed['feed'].get('title', None):
                user.name = feed['feed']['title']
                user.save()
            for item in feed['items']:
                if not user.status_set.filter(url=item['link']).count():
                    try:
                        text = item.get('title', '')[:140] + '<br/>' + str(item.get('content', ''))[:140]
                        pub_date = item.get('date_parsed', None) or datetime.now().timetuple()
                        pub_date = min(datetime.fromtimestamp(time.mktime(pub_date)), datetime.now()) # avoid pub_dates in the future
                        status = Status(user=user, url=item['link'], pub_date=pub_date, text=text)
                        status.save()
                    except Exception as e:
                        print("error for item %s: %s" % (str(item.get('url', None)), e))
                        raise
        except Exception as e:
            print("error parsing feed %s: %s" % (str(user.url), e))
            raise

if __name__ == '__main__':
    if 'fetch' in sys.argv:
        fetch()
    elif 'run' in sys.argv:
        while True:
            fetch()
            time.sleep(60)
    else:
        print('usage:  python3 scripts/rss.py [fetch|run]')
