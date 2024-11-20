import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 QMainWindow with VLayout and Button")

        # Create a central widget
        central_widget = custom_widget()

        # Set the central widget of the QMainWindow
        self.setCentralWidget(central_widget)



class custom_widget(QWidget):
    def __init__(self):
        super().__init__()
        main_vbox = QVBoxLayout()
        label = QLabel("Label")
        label_hbox = QHBoxLayout()
        label_hbox.addWidget(label)
        label_hbox.addStretch()

        button = QPushButton("hi")
        button_layout = QHBoxLayout()
        button_layout.addWidget(button)
        button_layout.addStretch()

        main_vbox.addLayout(label_hbox)
        main_vbox.addLayout(button_layout)
        main_vbox.addStretch()

        self.setLayout(main_vbox)
        

    







if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())