import tweepy
import csv

# consumer keys and access tokens, used for OAuth

consumer_key = 'twitter API consumer key'
consumer_secret = 'twitter API consumer secret'
access_token = 'twitter API access token'
access_token_secret = 'twitter API access token secret'

# OAuth process, using the keys and tokens

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creation of the actual interface, using authentication

api = tweepy.API(auth)

# search query based on phrase and hash tag
# your query goes inside quotation / -filter:retweets is used to leave aside retweets from search result

search_query = " " + " -filter:retweets"

# here you can define parameters as follow :

# ** lang: defines search language, default is en . you can see the full supported languages here :
# https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview

# ** result_type: defines the type of returned result. The values are : recent - popular - mixed

# ** tweet_mode : defines the type of returned tweets. extended returns the whole tweet text

# ** items(): defines the number of returned result per search query. The number of returned tweets
# may differ due to lack of tweets for searched query.

tweets = tweepy.Cursor(api.search, q=search_query, lang="en", result_type="recent", tweet_mode="extended").items(500)

# you can find other parameters like date here : http://docs.tweepy.org/en/latest/api.html#API.search

# write to file
tweet_set = open("your-directory/filename.csv", "w", newline='', encoding="utf-8")
writer = csv.writer(tweet_set)

# header for csv file . you can change the name
writer.writerow(['fulltext'])

# writes the tweets per rows
for item in tweets:
    writer.writerow([item.full_text])

