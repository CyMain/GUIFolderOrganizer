from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout, QHBoxLayout,
    QPushButton,
)
from PySide6.QtCore import (
    Signal
)
from PySide6.QtGui import(
    QTextDocument
)
from customWidgets import LogBoard


class FinishView(QWidget):
    back_home_requested = Signal()
    close_requested = Signal()
    revert_op_requested = Signal()

    def __init__(self):
        super().__init__()
        full_view_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        main_buttons_layout = QHBoxLayout()

        # completion_label = QLabel("Folder organized!!")
        self.completion_logs = LogBoard()

        # Back to home button
        self.back_to_home_button = QPushButton("Back to Home")
        self.back_to_home_button.clicked.connect(self.back_home_requested.emit)

        # Revert Operation button
        self.revert_operation_button = QPushButton("Revert")
        self.revert_operation_button.clicked.connect(self.revert_op_requested.emit)

        # Close Button
        self.close_button = QPushButton("Close the App")
        self.close_button.clicked.connect(self.close_requested.emit)

        # Piecing things together
        buttons_layout.addWidget(self.revert_operation_button)
        buttons_layout.addWidget(self.close_button)
        main_buttons_layout.addWidget(self.back_to_home_button)
        main_buttons_layout.addLayout(buttons_layout)
        full_view_layout.addWidget(self.completion_logs)
        full_view_layout.addLayout(main_buttons_layout)
        self.setLayout(full_view_layout)

    def setFinishLogsDoc(self, logDoc: QTextDocument):
        self.completion_logs.setDocument(logDoc)