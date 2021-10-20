from file_utils.file_handler import FileHandler
from twitter_utils.twython_api import TwythonApi


class TweetById:

	def __init__(self):
		
		self.file_handler = FileHandler()

		self.twython_api = TwythonApi()

	def run(self, api_config: dict, input_file: str, output_file: str, batch_size: int =100, col_index: int =0):

		dataset_reader = self.file_handler.reader(file_path=input_file)

		dataset_writer = self.file_handler.writer(file_path=output_file)

		tweet_api = self.twython_api.create_api(consumer_key=api_config["ck"], consumer_secret=api_config["cs"],
												access_token=api_config["at"], access_token_secret=api_config["as"])

		tweet_set = []

		for tweet in dataset_reader:

			tweet_id = self.file_handler.read_data(data=tweet, column_index=col_index)

			tweet_text = self.twython_api.fetch_tweet(api= tweet_api, tweet_id=tweet_id)

			if tweet_text:

				tweet_set.append(tweet_text)

			if len(tweet_set) > batch_size:

				self.file_handler.write_data(writer=dataset_writer, data=tweet_set)

				tweet_set = []
				