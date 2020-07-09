from twython import Twython
import csv

# consumer keys and access tokens, used for OAuth

consumer_key = 'twitter API consumer key'
consumer_secret = 'twitter API consumer secret'
access_token = 'twitter API access token'
access_token_secret = 'twitter API access token secret'

# OAuth process, using the keys and tokens

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

# input tweets id - can be a list of tweets in a .csv file ( one tweet per row )
# or a single tweet id

# path to your tweet list file ( can be .txt either )

tweet_ids = open("your-directory/filename.csv", "r")

# for a single tweet id remove the above line and below for loop with close statement
# then enter your id in id_list

id_list = []
counter = 0

for tweet in tweet_ids:
    id_list.append(tweet.rstrip('\n'))
    counter += 1

tweet_ids.close()

tweet_set = open("your-directory/filename.csv", "w", newline='', encoding="utf-8")

# write to file

writer = csv.writer(tweet_set)
writer.writerow(['fulltext'])

for tweet in id_list:

    counter -= 1
    print("remaining: ", counter)
    try:
        status = twitter.show_status(id=tweet)
        if status:
            writer.writerow([status['text']])
            print("file writen")
    except:
        print("not found - deleted or banned account")
        continue


