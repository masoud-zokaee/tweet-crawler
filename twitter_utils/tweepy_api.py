from tweepy import OAuthHandler, API


class TweepyApi:

    def __init__(self):
        
        pass

    def create_api(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
		Create tweepy api using consumer keys and access tokens.

		Args:
			consumer_key: twitter API consumer key
            consumer_secret: twitter API consumer secret
            access_token: twitter API access token
            access_token_secret: twitter API access token secret

		Returns:
            API object
		"""	

        # Set OAuth, using the keys and tokens

        auth = OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        # Creation of the actual interface, using authentication

        tweepy_api = API(auth)

        return tweepy_api

    def fetch_tweets(self, api, search_query: str, retweets: bool, language: str = "en",
                     result_type: str = "recent", tweet_mode: str = "extended", count: int = 100):
        """
		Fetch tweets based on input search query 
        and user defined search parameters

		Args:
            api: api object
			search_query: search query based on word, phrase, or hash tags
            retweets: leave aside retweets from search result or not
            language: defines search language, default is en . you can see the full supported languages here :
            https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview
            result_type: defines the type of returned result. The values are : recent - popular - mixed
            tweet_mode : defines the type of returned tweets. extended returns the whole tweet text
            count: defines the number of returned result per search query. The number of returned tweets
            may differ due to lack of tweets for searched query

		Returns:
            A list of fetched tweets
		"""

        if not retweets:

            search_query += " -filter:retweets"

        tweets = api.search_tweets(q=search_query, lang=language, result_type=result_type,
                                   tweet_mode=tweet_mode, count=count)

        tweet_set = [tweet.full_text for tweet in tweets]

        return tweet_set