from PySide6.QtWidgets import (
    QPushButton,
    QPlainTextEdit
)
from PySide6.QtCore import (
    Qt,
    QSize
)
from organizerScript import FolderOrganizer

class Organize_button(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        # self.clicked.connect(lambda: organize_folder("C:/Users/Cyrus/Pictures/artfrommytab"))


class LogBoard(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setMinimumSize(QSize(400, 200))
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 12px;
                border: 1px solid #3c3c3c;
                border-radius: 4px;
            }
        """)
