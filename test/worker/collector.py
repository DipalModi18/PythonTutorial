class Collector:
	args_parser = None
	name = None

	def __init__(self):
		self.args_parser = {
			'velocloud_host': '000',
			'velocloud_username': 'aaa',
			'velocloud_password': 'bbb',
			'velocloud_verify_ssl': 'ccc',
			'msp_name': 'ddd'
		}
		self.name = 'dipal'

	def get_arg(self, key):
		return self.args_parser[key]

	def validate_args(self):
		if not self.args_parser['velocloud_host'].strip():
			raise ValueError("Please provide a value for VELOCLOUD_HOST.")
			return False
		return True


def from_args():
	c = 10 + 5
	return c
