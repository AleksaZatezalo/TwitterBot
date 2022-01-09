"""
Description: Twitter bot main file.
Author: Aleksa Zatezalo
Date: January 9th, 2021
"""

"""
Description: Logs into twitter using Access tokens.
Author: Aleksa Zatezalo
Date: January 9th, 2021
"""

import tweepy
from requests.api import post
import urllib
from urllib.request import urlretrieve
from urllib.parse import urlparse
import os
import requests

from mediumPosting import *
from retweet import *

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


if __name__ == "__main__":
    # Post Article
    Title_Link_Post(URL)

    # Retweet Users 
    userRetweet(api, "@DarknetDiaries", 1)
    userRetweet(api, "@UofT", 1)
    userRetweet(api, "@siberxorg", 1)

    # Hashtag Retweet
    hashtag(api, "#yorklearns", 1)
