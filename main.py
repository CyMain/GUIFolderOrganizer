import sys
from organizerScript import organize
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
