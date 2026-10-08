from PySide6.QtCore import (
    QThread,
    Signal,
    Qt
)
from organizerScript import FolderOrganizer

class OrganizerWorker(QThread):
    log_signal = Signal(str)
    finished_signal = Signal()

    def __init__(self, target_path):
        super().__init__()
        self.target_path = target_path

    def run(self):
        organizer = FolderOrganizer(
            target_path=self.target_path,
            log_callback=self.log_signal.emit
            )
        try:
            organizer.organize_folder()
        except Exception as e:
            self.log_signal.emit(f"Error: {e}")
        finally:
            self.finished_signal.emit()
