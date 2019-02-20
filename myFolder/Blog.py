# This class is used in test_mock2

import requests


class Blog:
	def __init__(self, name):
		self.name = name

	def posts(self):
		response = requests.get("https://jsonplaceholder.typicode.com/posts")
		return response.json()

	def __repr__(self):
		return '<Blog: {}>'.format(self.name)
