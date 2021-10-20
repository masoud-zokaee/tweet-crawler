from main_builder.tweet_by_id import TweetById

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

	tweet_by_id = TweetById()

	tweet_by_id.run(api_config=api_config,
					input_file="your-directory/filename.csv",
					output_file="your-directory/filename.csv")