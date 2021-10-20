# Tweet Crawler

Crawl tweet texts from twitter using twitter API

## Getting Started

Copy python files or clone the entire repository and do the followings:

1- Inside main_courser and main_by_id files replace 
   your twitter API consumer keys and access tokens

2- Enter your search query ( word - hashtag - phrase ) and other 
   required parameters inside search_config 

2.1 - Or enter your tweet id file path ( for main_by_id )

3- Also choose your output .csv file directory and file name

## Prerequisites

Required python libraries 

1- tweepy 2- twython 3- csv

you can use commands like

```
pip install tweepy

pip install csv

pip install twython

```

or you can simply use the ***requirements.txt*** file to install all requirements

## Files description 

1- tweet_cursor.py : crawl twitter for tweets based on an entry search query, tweets date can
back to previous weeks till now

2- tweet_by_id.py : crawl twitter for tweets based on tweet ids. tweet id can be a list of ids stored 
in a .csv or .txt file. you can specify index of id column in case of multiple columns(default is 0)

## Useful links

Tweepy documents : 

http://docs.tweepy.org/en/latest/api.html

A guide to successfully apply to access Twitter APIs : 

https://realsocialseo.com/successfully-apply-to-access-twitter-apis/

## Some Tips 

Twitter API's have some limits in using and retrieving tweets, like the number of requests 

and post / get endpoints. you can find the complete details here :

https://developer.twitter.com/en/docs/basics/rate-limits  
