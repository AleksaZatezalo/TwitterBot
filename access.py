import tweepy
from requests.api import post
import urllib
from urllib.request import urlretrieve
from urllib.parse import urlparse
import os
import requests

# Tokens
API_KEY = "IIOiVHkh1eIPSPUG9WqVfiZu3"
API_SECRET_KEY = "yDUzG1zRBHrjetht4CIDpShEJE5YYsxvxawbzaoGHGwgD6C0kf"
API_ACCESS_TOKEN = "1344441776539652096-5UlqLhAmjOafvmPaj7Xg9C165QwaK1"
API_ACCESS_SECRET = "9zsTQsVg6rQOXCXeLnCxvJRYj5Az2QXM5bQG7EZZjYuPQ"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOe%2BXwEAAAAAuvnS8EG1EoZIEoushblaStpVoDw%3DbT4qXYwNuzqClc0qrUBgLpWXFPlKtvhSXti8soorR21v289NMR"

# Authentication
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(API_ACCESS_TOKEN, API_ACCESS_SECRET)
api = tweepy.API(auth)

post("https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@aleksazatezalo")