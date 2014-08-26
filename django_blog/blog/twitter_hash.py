# -*- coding: utf-8 -*-
import oauth2 as oauth
import json
import os
import re

def twitter_hash(max=5, hasht="python"):
	# dados do app no Twitter DEV
    API_KEY = os.environ['API_KEY']
    API_SECRET = os.environ['API_SECRET']

    TOKEN = os.environ['TOKEN']
    TOKEN_SECRET = os.environ['TOKEN_SECRET']

    # Login

    #import ipdb; ipdb.set_trace()
    consumer = oauth.Consumer(key=API_KEY, secret=API_SECRET)
    token = oauth.Token(key=TOKEN, secret=TOKEN_SECRET)
    client = oauth.Client(consumer, token)
    url = "https://api.twitter.com/1.1/search/tweets.json?q=%23{0}&count={1}"
    search_url = url.format(hasht, str(max))

    response, data = client.request(search_url)

    tweets = json.loads(data)

    if tweets.get('statuses'):
        in_link = u'<a href="{0}" target="_blank">{0}</a>'
        in_hash = u'<a href="javascript:;" class="hash">{0}</a>'
        user = u'<a href="http://www.twitter.com/{0}" target="_blank">{0}</a>'
        for i in tweets.get('statuses'):
            for link in re.findall(r"https?://[^\s]+[^W]", i.get('text')):
                i['text'] = i['text'].replace(link, in_link.format(link))
            for hs in re.findall(r"#[\w]+[^\s]", i.get('text')):
                i['text'] = i['text'].replace(hs, in_hash.format(hs))
            for u in re.findall(r"@[\w]+[^\s|,]+[^\W]", i.get('text')):
                i['text'] = i['text'].replace(u, user.format(u.replace('@','')))


    return tweets.get('statuses')

    # for tweet in tweets['statuses']:
    #     print "Autor: %s" % tweet['user']['name'], tweet['text']
