import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import time

# search query

phrase_to_search = ""

# consumer keys and access tokens, used for OAuth

consumer_key = 'twitter API consumer key'
consumer_secret = 'twitter API consumer secret'
access_token = 'twitter API access token'
access_token_secret = 'twitter API access token secret'

g = []


class StdOutListener(StreamListener):
    def on_data(self, data):
        # Streaming API. Streaming API listens for live tweets
        print(data)
        g.append(data)
        time.sleep(2)
        return True

    # To print the status if an error happens
    def on_error(self, status):
        print(status)


def call_api(stream, phrase):
    # If the time crosses the amount of time mentioned by t_end, then the tweet scrapping stops
    try:
        stream.filter(track=[phrase])
    except Exception as e:
        print(e)

    # If the stream is already connected, the following will disconnect the stream and reconnect it
    if "Stream object already connected!" in str(e):
        stream.disconnect()
        print("connecting again")
        stream.filter(track=[phrase])


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, listener)
    call_api(stream, phrase_to_search)
