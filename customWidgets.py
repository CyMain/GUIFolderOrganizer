from PySide6.QtWidgets import QPushButton

class Organize_button(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.clicked.connect()
