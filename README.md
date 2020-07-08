# Tweet Crawler

Crawl tweet texts from twitter with twitter API

## Getting Started

Copy or download python files and do followings:

1- replace your twitter API consumer keys and access tokens

2- enter your search query ( word - hashtag - phrase )

3- choose your output .csv file directory and file name

### Prerequisites

you need two python library 

1- tweepy 2- csv

you can use commands like

```
pip install tweepy

pip install csv

```

## Files description 

1- tweet_cursor.py : crawl twitter for tweets based on entry search query, tweets date can
back to previous weeks till now

2- tweet_stream.py : crawl twitter for tweets based on entry search query using stream behavior,
tweets which have been published from the moment you run the code will be returned. 

## Useful links

Tweepy documents : 

http://docs.tweepy.org/en/latest/api.html

A guide to successfully apply to access Twitter APIs : 

https://realsocialseo.com/successfully-apply-to-access-twitter-apis/

### Some Tips 

twitter API's have some limits in using and retrieving tweets like number of requests 

and post / get endpoints. you can find the complete details here :

https://developer.twitter.com/en/docs/basics/rate-limits  
