from PySide6.QtWidgets import QPushButton
from organizerScript import FolderOrganizer

class Organize_button(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        # self.clicked.connect(lambda: organize_folder("C:/Users/Cyrus/Pictures/artfrommytab"))
