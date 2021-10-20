from twython import Twython


class TwythonApi:

    def __init__(self):

        pass

    def create_api(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
		Create twython api using consumer keys and access tokens.

		Args:
			consumer_key: twitter API consumer key
            consumer_secret: twitter API consumer secret
            access_token: twitter API access token
            access_token_secret: twitter API access token secret

		Returns:
            API object
		"""	

        # Set OAuth, using the keys and tokens

        twython_api = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

        return twython_api

    def fetch_tweet(self, api, tweet_id: str):
        """
		Fetch tweet based on input id

		Args:
            api: api object
			tweet_id: id of tweet post

		Returns:
            tweet if exist or corresponding error
		"""

        try:

            status = api.show_status(id=tweet_id)

            tweet = status["text"]

        except:

            tweet = ""   

        return tweet
