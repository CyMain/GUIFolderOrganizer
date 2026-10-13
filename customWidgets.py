from PySide6.QtWidgets import (
    QPlainTextEdit
)
from PySide6.QtCore import (
    QSize
)

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

    def getLogsDocument(self):
        return self.document()