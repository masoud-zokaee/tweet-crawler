from file_utils.file_handler import FileHandler
from twitter_utils.tweepy_api import TweepyApi


class TweetCursor:

    def __init__(self):

        self.file_handler = FileHandler()

        self.tweepy_api = TweepyApi()

    def run(self, api_config: dict, search_config: dict, output_file: str):

        tweet_writer = self.file_handler.writer(file_path=output_file)

        tweet_api = self.tweepy_api.create_api(consumer_key=api_config["ck"], consumer_secret=api_config["cs"],
                                                access_token=api_config["at"], access_token_secret=api_config["as"])

        tweet_set = self.tweepy_api.fetch_tweets(api=tweet_api, search_query=search_config["sq"], 
                                                 retweets=search_config["re"], language=search_config["ln"],
                                                 result_type=search_config["rt"], tweet_mode=search_config["tm"],
                                                 count=search_config["ct"])

        self.file_handler.write_data(writer=tweet_writer, data=tweet_set)
