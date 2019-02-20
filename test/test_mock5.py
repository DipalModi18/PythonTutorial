from unittest import mock, TestCase, expectedFailure
from test.worker.collector import Collector
import unittest

mock_args_parser = {
	'velocloud_host': 'zzz',
	'velocloud_username': 'yyy',
	'velocloud_password': 'xxx',
	'velocloud_verify_ssl': 'www',
	'msp_name': 'vvv'
}


class TestCollector5(TestCase):

	# @mock.patch.object(Collector, 'validate_args')
	# def test_validate_args(self, mock_validate_args):
	# 	print('test_validate_args')
	# 	# mock_validate_args.return_value = False
	# 	# print(mock_validate_args())
	# 	collector = Collector()
	# 	print(collector.validate_args())

	# By default patch() will fail to replace attributes that do not exist.
	# If you pass in create = True, and the attribute does not exist, patch will create the attribute
	# for you when the patched function is called, and delete it again after the patched function has exited.
	@mock.patch.dict(Collector.args_parser, {'newkey': 'newvalue'})
	def test_args_parser(self, MockArgsParser):
		print('test_args_parser')
		collector = Collector()
		print(collector.args_parser)

	@mock.patch.object(Collector, 'name', 'modi')
	def test_name(self):
		print('test_name')
		collector = Collector()
		print(collector.name)

	def test_collect(self):
		pass
