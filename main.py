import sys, pathlib
from organizerScript import FolderOrganizer
from organizerWorker import OrganizerWorker
from customWidgets import (
    LogBoard
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QProgressBar
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
        self.target_path = ""


    ### Various Pages/Views of the Application
    def ui_setup(self):
        self.setWindowTitle("FolderOrganizerApp")
        self.setMinimumSize(QSize(500, 400))
        self.resize(600, 500)

        appHeroLabel = QLabel("Welcome to my organizer App!!")
        appHeroLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        appHeroImageLabel = QLabel()
        appHeroImageLabel.setPixmap(QPixmap("./assets/images/CharaHolidays.jpg"))
        appHeroImageLabel.setMaximumSize(QSize(400, 200))
        appHeroImageLabel.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(appHeroImageLabel)
        layout.addWidget(appHeroLabel)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

    def log_view_setup(self):
        self.log_board = LogBoard()

        self.organize_progress_bar = QProgressBar()
        self.organize_progress_bar.setRange(0, 100)
        self.organize_progress_bar.setValue(0)


        logs_layout = QVBoxLayout()
        logs_layout.addWidget(self.log_board)
        logs_layout.addWidget(self.organize_progress_bar)

        logs_container = QWidget()
        logs_container.setLayout(logs_layout)

        self.setCentralWidget(logs_container)

    def finish_view_setup(self):
        """Renders the finished screen. To be used when the app has finished an organizing operation."""


    ### Various App methods.
    def folder_button_clicked(self):
        dir_store = QFileDialog.getExistingDirectory(self, "Select a Folder to Organize");
        if dir_store:
            self.directory_field.setText(dir_store)
        else:
            pass

    def directory_chosen(self, text):
        print("Directory: ", text)
        if text != "":
            if not pathlib.Path(text).exists():
                print(f"{pathlib.Path(text)} does not exist.")
                return
            self.organize_button.setEnabled(True)
        else:
            self.organize_button.setDisabled(True)

    def organize_button_clicked(self):
        if self.organize_button.isEnabled():
            self.organize_dir()
        else:
            print("Organize button is diabled.")

    def organize_dir(self):
        self.log_view_setup()
        target_path = self.directory_field.text().strip()

        self.log_board.clear()

        self.worker = OrganizerWorker(target_path=target_path)

        self.worker.log_signal.connect(self.append_log)
        self.worker.finished_signal.connect(self.on_finished)

        self.worker.start()

    def append_log(self, text: str):
        """Receives signal from the worker thread and updates the log text box."""
        self.log_board.appendPlainText(text)

    def on_finished(self):
        print("Organization Completo!!")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
