import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTabWidget
from controller import controller

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 QMainWindow with VLayout and Button")
        #create tab_widget:
        self.tab_widget = QTabWidget()

        # Create widgets
        self.controller = controller()

        #add tabs
        self.tab_widget.addTab(self.controller, "Controller")
        # Set the central widget of the QMainWindow
        self.setCentralWidget(self.tab_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
