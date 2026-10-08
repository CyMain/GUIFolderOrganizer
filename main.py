import sys
from organizerScript import FolderOrganizer
from customWidgets import Organize_button
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFileDialog
    )
from PySide6.QtCore import (
    Qt,
    QSize
)
from PySide6.QtGui import (
    QPixmap
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_setup()
        self.organizerObj = FolderOrganizer()

    def ui_setup(self):
        self.setWindowTitle("FolderOrganizerApp")
        self.setMinimumSize(QSize(500, 400))

        appHeroLabel = QLabel("Welcome to my organizer App!!")
        appHeroLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        appHeroImageLabel = QLabel()
        appHeroImageLabel.setPixmap(QPixmap("./assets/images/CharaHolidays.jpg"))
        appHeroImageLabel.setMaximumSize(QSize(400, 200))

        layout = QVBoxLayout()
        layout.addWidget(appHeroImageLabel)
        layout.addWidget(appHeroLabel)

        container = QWidget()
        container.setLayout(layout)


        self.directory_field = QLineEdit()
        self.directory_field.textChanged.connect(self.directory_chosen)

        self.chooseFolderButton = QPushButton("Choose Folder")
        self.chooseFolderButton.clicked.connect(self.folder_button_clicked)

        directory_layout = QHBoxLayout()
        directory_layout.addWidget(self.directory_field)
        directory_layout.addWidget(self.chooseFolderButton)
        
        buttons_container = QWidget()
        buttons_container.setLayout(directory_layout)

        self.organize_button = QPushButton("Organize")
        self.organize_button.setDisabled(True)
        self.organize_button.clicked.connect(self.organize_dir)


        app_layout = QVBoxLayout()
        app_layout.addWidget(container)
        app_layout.addWidget(buttons_container)
        app_layout.addWidget(self.organize_button)

        app_container = QWidget()
        app_container.setLayout(app_layout)

        self.setCentralWidget(app_container)

    def folder_button_clicked(self):
        dir_store = QFileDialog.getExistingDirectory(self, "Select a Folder to Organize");
        if dir_store:
            self.directory_field.setText(dir_store)
        else:
            pass

    def directory_chosen(self, text):
        print("Directory: ", text)
        self.organizerObj.setPath(text)
        if text != "":
            self.organize_button.setEnabled(True)
        else:
            self.organize_button.setDisabled(True)

    def organize_button_clicked(self):
        if self.organize_button.isEnabled():
            self.organize_dir()
        else:
            print("Organize button is diabled.")

    def organize_dir(self):
        self.organizerObj.organize_folder()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
