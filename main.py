import sys
from views import HomeView, LogView, FinishView
from organizerWorker import OrganizerWorker
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget
    )
from PySide6.QtCore import (
    QSize,
    QTimer
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FolderOrganizerApp")
        self.setMinimumSize(QSize(500, 400))
        self.resize(600, 500)
        self.target_path = ""

        # 0. Create operation stack
        self.operations = []

        # 1. Create the router/stack
        self.view_stack = QStackedWidget()
        self.setCentralWidget(self.view_stack)

        # 2. Instantiate individual views
        self.home_view = HomeView()
        self.log_view = LogView()
        self.finish_view = FinishView()

        # 3. Add them to the stack (index 0, 1, 2)
        self.view_stack.addWidget(self.home_view)
        self.view_stack.addWidget(self.log_view)
        self.view_stack.addWidget(self.finish_view)

        # 4. Connect View signals to MainWindow
        self.home_view.start_organization.connect(self.organize_dir)
        self.finish_view.back_home_requested.connect(lambda: self.view_stack.setCurrentIndex(0))
        self.finish_view.close_requested.connect(self.close)
        self.finish_view.revert_op_requested.connect(self.revert_op)

    def organize_dir(self, target_path):
        self.target_path = target_path
        
        # Switch the UI to the log view (index 1)
        self.view_stack.setCurrentIndex(1)
        self.log_view.log_board.clear()

        # Start your background process cleanly
        self.worker = OrganizerWorker(target_path=self.target_path)
        self.worker.log_signal.connect(self.append_log)
        self.worker.finished_signal.connect(self.on_finished)
        self.worker.start()

    def append_log(self, message: dict):
        # Safely pushes logs right down into the specific widget
        if message["type"] == "move":
            self.operations.append({
                "operation":message["operation"],
                "prev_file_folder": message["prev_file_folder"],
                "curr_file_folder": message["curr_file_folder"],
                "file_name": message["file_name"],
                "message": message["message"]
            })
        if message["type"] == "folder":
            self.operations.append({
                "message":message["message"],
                "operation":message["operation"],
                "folder_name":message["folder_name"]
            })
        
        self.log_view.log_board.appendPlainText(f"{message["operation"]}: {message["message"]}")

    def append_revert_log(self, message: dict):
            # Safely pushes logs right down into the specific widget
            if message["type"] == "move":
                self.operations.append({
                    "operation":message["operation"],
                    "prev_file_folder": message["prev_file_folder"],
                    "curr_file_folder": message["curr_file_folder"],
                    "file_name": message["file_name"],
                    "message": message["message"]
                })
            if message["type"] == "folder":
                self.operations.append({
                    "message":message["message"],
                    "operation":message["operation"],
                    "folder_name":message["folder_name"]
                })
            
            self.finish_view.completion_logs.appendPlainText(f"{message["operation"]}: {message["message"]}")

    def on_finished(self):
        print("Organization Completo!!")
        # Switch to finish view (index 2) after brief delay
        QTimer.singleShot(2, lambda: self.view_stack.setCurrentIndex(2))
        self.finish_view.setFinishLogsDoc(self.log_view.getLogsDoc())

    def on_revert_finished(self):
            print("Reverting Complete!!")
            self.finish_view.completion_logs.appendPlainText("Reverting Complete.")

    def revert_op(self):
        self.worker = OrganizerWorker(
            target_path=self.target_path
        )
        self.worker.log_signal.connect(self.append_revert_log)
        self.worker.finished_signal.connect(self.on_revert_finished)
        self.worker.revert_operation(operations=self.operations)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
