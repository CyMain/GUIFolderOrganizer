import pathlib
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout, QHBoxLayout,
    QLineEdit,
    QPushButton,
)
from PySide6.QtCore import (
    Qt,
    QSize,
    Signal
)
from PySide6.QtGui import (
    QPixmap
)


class HomeView(QWidget):
    folder_selected = Signal(str)
    start_organization = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui_setup()

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
            self.organize_button.clicked.connect(self.on_organize_clicked)
    
    
            app_layout = QVBoxLayout()
            app_layout.addWidget(container)
            app_layout.addWidget(buttons_container)
            app_layout.addWidget(self.organize_button)
    
            self.setLayout(app_layout)

    def folder_button_clicked(self):
        from PySide6.QtWidgets import QFileDialog
        dir_store = QFileDialog.getExistingDirectory(self, "Select a Folder to Organize")
        if dir_store:
            self.directory_field.setText(dir_store)

    def directory_chosen(self, text):
        if text and pathlib.Path(text).exists():
            self.organize_button.setEnabled(True)
            self.folder_selected.emit(text) # Let the app know a valid path was picked
        else:
            self.organize_button.setDisabled(True)

    def on_organize_clicked(self):
        # Just emit the signal with the path! The view doesn't process the worker thread.
        self.start_organization.emit(self.directory_field.text().strip())
        