# WebSocial

WebSocial is an open source, federated social networking platform that is mediated by RSS/Atom.  Like other social networks, it allows users to "microblog" and follow other users whose posts will appear in their feeds.  Unlike other services, it allows users to follow RSS feeds as if they were other users.  WebSocial also provides an RSS feed for each user, enabling users on other servers to follow them, whether they're using another WebSocial server, or an RSS reader.

Disclaimer: WebSocial is currently in prototype status, and needs a new name, as there is already an existing, unrelated service by this name.  I have no affiliation with said service.

## Running It

**To install dependencies**:

    pip3 install -r requirements.txt

**To create the development database**:

    python3 manage.py migrate

This will create db.sqlite3, which will not be versioned due to settings in the .gitignore file.

**To run the development web server** on port 8000 (runs until killed with Ctrl+C, so do this in its own terminal window or tab):

    python3 manage.py runserver

You can view the main page by going to http://localhost:8080 in a browser.

**To run the RSS process** (polls followed RSS feeds every 10 seconds until killed with Ctrl+C, so do this in its own terminal window or tab as well):

    python3 scripts/rss.py run

Use "fetch" instead of "run" to fetch followed RSS feeds once but not continue to poll.
