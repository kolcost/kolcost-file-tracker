import os
import queue

class FileTracker:
    is_monitoring = False
    queue = queue.Queue()

    def __init__(self, directory_path: str, period: int=0):
        self.directory_path = directory_path
        self.period = period
        self.files = [file for file in os.listdir(self.directory_path) if os.path.isfile(os.path.join(self.directory_path, file))]

    def start_monitoring(self):
        self.is_monitoring = True
        while self.is_monitoring:
            pass


    def stop_monitoring(self):
        self.is_monitoring = False