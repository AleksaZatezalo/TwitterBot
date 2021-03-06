"""
Description: Function Libary to Post Medium Article.
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

URL = "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@aleksazatezalo"

# URL To Fetch Latest Post
def fetch_article(url):
    """
    Takes a medium URL and fetches the article. 
    """

    response = requests.get(url)
    posts = response.json()
    if posts["status"] == "ok":
        posts = posts["items"]
        for post in posts:
            post_title = post["title"]
            post_url = post["link"]
            post_image = post["thumbnail"]
            return {"title": post_title, "thumbnail": post_image, "link": post_url}

def Title_Link_Post(url):
    """
    Uses a given URL and fetch_article to craft a post with a corresponding title and link. 
    """

    post_dict = fetch_article(url)
    title = post_dict['title']
    link = post_dict["link"]
    post_str = f'Hey, check out my most recent article on medium.com! It is called ' + "\"" + title + "\"" + ".\n" + link
    return post_str
