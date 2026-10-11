from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout, QHBoxLayout,
    QPushButton,
)
from PySide6.QtCore import (
    Signal
)


class FinishView(QWidget):
    back_home_requested = Signal()
    close_requested = Signal()

    def __init__(self):
        super().__init__()
        full_view_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        main_buttons_layout = QHBoxLayout()

        completion_label = QLabel("Folder organized!!")
        back_to_home_button = QPushButton("Back to Home")
        back_to_home_button.clicked.connect(self.back_home_requested.emit)
        
        revert_operation_button = QPushButton("Revert")
        
        close_button = QPushButton("Close the App")
        close_button.clicked.connect(self.close_requested.emit)

        buttons_layout.addWidget(revert_operation_button)
        buttons_layout.addWidget(close_button)
        main_buttons_layout.addWidget(back_to_home_button)
        main_buttons_layout.addLayout(buttons_layout)
        full_view_layout.addWidget(completion_label)
        full_view_layout.addLayout(main_buttons_layout)
        self.setLayout(full_view_layout)