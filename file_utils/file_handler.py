import csv

class FileHandler:

	def __init__(self):

		pass

	def reader(self, file_path: str, skip_header: bool =False):

		input_file = open(file_path, "r")

		if skip_header:

			input_file.readline()

		return input_file

	def writer(self, file_path: str, header_name: str ="fulltext"):

		output_file = open(file_path, "w", newline='', encoding="utf-8")

		writer = csv.writer(output_file)

		writer.writerow([header_name])

		return writer

	def read_data(self, data, column_index):

		data = data.strip()

		tweet_id = data.split(",")[column_index]

		return tweet_id

	def write_data(self, writer, data):

		for item in data:

			writer.writerow([item])