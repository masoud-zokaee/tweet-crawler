from main_builder.tweet_cursor import TweetCursor

if __name__ == "__main__":

	api_config = {
		# consumer_key
		"ck": "",
		# consumer_secret
		"cs": "",
		# access_token
		"at": "",
		# access_token_secret
		"as": ""
	}

	search_config = {
		# search_query
		"sq": "",
		# retweets
		"re": False,
		# language
		"ln": "en",
		# result_type
		"rt": "recent",
		# tweet_mode
		"tm": "extended",
		# num_items
		"ct": 100,
	}

	tweet_cursor = TweetCursor()

	tweet_cursor.run(api_config=api_config,
					 search_config=search_config,
					 output_file="your-directory/filename.csv")
