import os
import time

from File_tracker.file_tracker import FileTracker
import unittest

class TestFileTracker(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.txt"
        with open(os.path.join('.', 'tests', self.test_file), 'w') as f:
            f.write("initial content")

        self.tracker: FileTracker = FileTracker(directory_path='./tests/', )
        self.tracker.start_monitoring()

    def tearDown(self):
        os.remove(os.path.join('.', 'tests', self.test_file))
        self.tracker.stop_monitoring()


    def test_add_file(self):

        file_test_name = "new_test_file"

        with open(os.path.join('.', 'tests', file_test_name)):
            pass

        time.sleep(0.5)

        response:str = self.tracker.queue.get()

        os.remove(os.path.join('.', 'tests', file_test_name))

        self.assertIsNotNone(response, "Queue is empty" '')
        self.assertTrue(response.endswith(os.path.join('.','tests', file_test_name)), 'Uncorrected file path')


    def test_remove_file(self):

        os.remove(os.path.join('.', 'tests', self.test_file))

        time.sleep(0.5)

        response:str = self.tracker.queue.get()
        self.assertIsNotNone(response, "Queue is empty" '')
        self.assertTrue(response.endswith(os.path.join('.', 'tests', self.test_file)), 'Uncorrected file path')


    def test_edit_file(self):

        with open(os.path.join('.', 'tests', self.test_file), 'w') as f:
            f.write('test content')

        time.sleep(0.5)

        response:str = self.tracker.queue.get()
        self.assertIsNotNone(response, "Queue is empty" '')
        self.assertTrue(response.endswith(os.path.join('.', 'tests', self.test_file)), 'Uncorrected file path')