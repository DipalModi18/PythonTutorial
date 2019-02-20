import unittest
from unittest import mock, TestCase
from test.worker.collector import Collector


with mock.patch.object(Collector, 'get_arg', return_value='333') as mock_method:
	inst = Collector()
	print(inst.get_arg('hhh'))


foo = {'key': 'value'}
original = foo.copy()
with mock.patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
	print(foo['newkey'])


# if __name__ == '__main__':
# 	unittest.main()
