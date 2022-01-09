"""
Description: Retweets posts from specific organisations.
Author: Aleksa Zatezalo
Date: January 9th, 2021
"""

import tweepy
from time import sleep

def hashtag(api, hashtag, num):
    """
    Takes tweepy api and hashtag as inputs. Retweets 3 corrisponding hashtags. 
    """

    for tweet in tweepy.Cursor(api.search, hashtag).items(num):
        try:
            print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

            tweet.retweet()
            print('Retweet published successfully.')

            # Where sleep(10), sleep is measured in seconds.
            # Change 10 to amount of seconds you want to have in-between retweets.
            # Read Twitter's rules on automation. Don't spam!
            sleep(10)

        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)

        except StopIteration:
            break
    return 0

def userRetweet(api, user, num):
    """
    Retweets users last specific post. Takes tweepy api and user string as input,
    """

    last_tweets = api.user_timeline(user, num)

    for tweet in tweepy.Cursor(last_tweets, hashtag).items(num):
        try:
            tweet.retweet()
            print('Retweet published successfully.')

            # Where sleep(10), sleep is measured in seconds.
            # Change 10 to amount of seconds you want to have in-between retweets.
            # Read Twitter's rules on automation. Don't spam!
            sleep(10)

        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)

        except StopIteration:
            break
    return 0