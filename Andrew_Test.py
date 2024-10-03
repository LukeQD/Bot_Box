import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 QMainWindow with VLayout and Button")
        widget=TestWidget()
        self.setCentralWidget(widget)
        


class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_vbox= QVBoxLayout()
        name_hbox=QHBoxLayout()

        name_hbox.addWidget(QLabel("Name"))
        self.text_edit= QLineEdit()
        name_hbox.addWidget(self.text_edit)
        name_hbox.addStretch()

        button_hbox=QHBoxLayout()
        button= QPushButton("Press me")
        button.pressed.connect(self.button_pressed)
        button_hbox.addWidget(button)
        button_hbox.addStretch()






        main_vbox.addLayout(name_hbox)
        main_vbox.addLayout(button_hbox)
        main_vbox.addStretch()

        self.setLayout(main_vbox)

    def button_pressed(self):
        name=self.text_edit.text()
        print(f"my name is {name}")





  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    "Q application from pyside"
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
