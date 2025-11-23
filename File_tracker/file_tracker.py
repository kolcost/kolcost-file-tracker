import os
import queue

class FileTracker:
    files = []

    def __init__(self, directory_path, period=0):
        self.directory_path = directory_path
        self.period = period
        self.queue = queue.Queue()

    def start_monitoring(self):
        pass

    def stop_monitoring(self):
        pass