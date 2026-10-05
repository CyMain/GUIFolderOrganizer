import sys
from organizerScript import organize_folder
from customWidgets import Organize_button
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
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

        appHeroLabel = QLabel("Welcome to my organizer App!!")
        appHeroLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        appHeroImageLabel = QLabel()
        appHeroImageLabel.setPixmap(QPixmap("./assets/images/CharaHolidays.jpg"))

        startButton = Organize_button("Start")
        startButton.clicked.connect(organize_folder)


        layout = QVBoxLayout()
        layout.addWidget(appHeroImageLabel)
        layout.addWidget(appHeroLabel)
        layout.addWidget(startButton)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
