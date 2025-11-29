import os
import time

from File_tracker.file_tracker import FileTracker
import unittest

LAST_CHANGES: tuple[str, str] = ('PATH_TO_FILE', 'ACTION_ON_FILE')

def communicator(path: str, action:str):
    global LAST_CHANGES
    LAST_CHANGES = (path, action)

class TestFileTracker(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.txt"
        with open(os.path.join('.', 'tests', self.test_file), 'w') as f:
            f.write("initial content")

        self.tracker: FileTracker = FileTracker(directory_path='./tests/', )
        self.tracker.start_monitoring()
        self.tracker.add_handler(handler=communicator)

    def tearDown(self):
        os.remove(os.path.join('.', 'tests', self.test_file))
        self.tracker.stop_monitoring()
        self.tracker.remove_handler(handler=communicator)




    def test_file_creation(self):
        file_test_name = "new_test_file.txt"
        with open(os.path.join('.', 'tests', file_test_name)):
            pass
        time.sleep(0.5)

        self.assertTrue(LAST_CHANGES[0].endswith(file_test_name), msg=f'(File creation):  Wrong file \n {LAST_CHANGES}')
        self.assertTrue(LAST_CHANGES[1] == 'creation', msg=f'(File creation):  Wrong action \n {LAST_CHANGES}')

        os.remove(os.path.join('.', 'tests', file_test_name))



    def test_file_delete(self):

        os.remove(os.path.join('.', 'tests', self.test_file))

        time.sleep(0.5)

        self.assertTrue(LAST_CHANGES[0].endswith(self.test_file), msg=f'(File delete):  Wrong file \n {LAST_CHANGES}')
        self.assertTrue(LAST_CHANGES[1] == 'creation', msg=f'(File delete):  Wrong action \n {LAST_CHANGES}')



    def test_edit_file(self):

        with open(os.path.join('.', 'tests', self.test_file), 'w') as f:
            f.write('test content')

        time.sleep(0.5)

        self.assertTrue(LAST_CHANGES[0].endswith(self.test_file), msg=f'(File edit):  Wrong file \n {LAST_CHANGES}')
        self.assertTrue(LAST_CHANGES[1] == 'creation', msg=f'(File edit):  Wrong action \n {LAST_CHANGES}')


