from customWidgets import LogBoard
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QProgressBar
)


class LogView(QWidget):
    def __init__(self):
        super().__init__()
        self.log_board = LogBoard()
        self.organize_progress_bar = QProgressBar()
        self.organize_progress_bar.setRange(0, 100)
        self.organize_progress_bar.setValue(0)

        logs_layout = QVBoxLayout()
        logs_layout.addWidget(self.log_board)
        logs_layout.addWidget(self.organize_progress_bar)
        self.setLayout(logs_layout)