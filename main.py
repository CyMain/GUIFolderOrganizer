import sys
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
        self.startButton = Organize_button("Start")
        self.startButton.clicked.connect(self.organize_button_clicked)

        directory_layout = QHBoxLayout()
        directory_layout.addWidget(self.directory_field)
        directory_layout.addWidget(self.startButton)
        
        buttons_container = QWidget()
        buttons_container.setLayout(directory_layout)


        app_layout = QVBoxLayout()
        app_layout.addWidget(container)
        app_layout.addWidget(buttons_container)

        app_container = QWidget()
        app_container.setLayout(app_layout)

        self.setCentralWidget(app_container)

    def organize_button_clicked(self):
        dir_store = QFileDialog.getExistingDirectory(self, "Select a Folder to Organize");
        if dir_store:
            self.directory_field.setText(dir_store)
        else:
            pass

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
