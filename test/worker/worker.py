"""Used in mocking_classes.py"""

import os


class Helper:

    def __init__(self, path):
        self.path = path

    def get_path(self):
        base_path = os.getcwd()
        print('path in Helper.get_path: ', base_path)  # Will not be called as it is mocked
        return os.path.join(base_path, self.path)

    def get_a(self):
        return 'a'

    def get_b(self):
        return 'b'


class Worker:

    def __init__(self):
        self.helper = Helper('db')

    def work(self):
        path = self.helper.get_path()
        print('Working on ' + path)
        return path
