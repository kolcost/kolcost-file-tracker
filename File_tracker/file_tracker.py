import os
import queue
import time


class FileTracker:
    is_monitoring = False
    handlers = []


    def __init__(self, directory_path: str, period: int=0) -> None:
        self.directory_path = directory_path
        self.period = period
        self.files = [file for file in os.listdir(self.directory_path) if os.path.isfile(os.path.join(self.directory_path, file))]


    def start_monitoring(self) -> None:
        self.is_monitoring = True
        last_files = self.files
        lastest_files_timestamp = self.latest_file_changes(last_files)



        while self.is_monitoring:
            time.sleep(self.period)
            actual_files = [file for file in os.listdir(self.directory_path) if os.path.isfile(os.path.join(self.directory_path, file))]



            last_files = actual_files



    def stop_monitoring(self) -> None:
        self.is_monitoring = False

    def latest_file_changes(self, files:list[str]) -> dict[str, float]:
        latest_changes = {}
        for file in files:
            latest_changes[os.path.join(self.directory_path, file)] = os.path.getmtime(file)

        return latest_changes

    def sending_events_to_handlers(self, path: str, action:str) -> None:
        for handler in self.handlers:
            handler(path, action)
