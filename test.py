import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout,QPushButton
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QRect

class RectangleWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(100, 100, 255))  # Set color for the rectangle

        # Get the widget's dimensions
        widget_width = self.width()
        widget_height = self.height()

        # Define the size of the rectangle
        rect_width = widget_width // 2
        rect_height = widget_height // 2

        # Calculate the top-left corner of the rectangle to center it
        x = (widget_width - rect_width) // 2
        y = (widget_height - rect_height) // 2

        # Draw the rectangle
        painter.drawRect(QRect(x, y, rect_width, rect_height))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window with Rectangle")

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout
        hbox_layout = QHBoxLayout()
        button = QPushButton("YES")
        # Create an instance of RectangleWidget
        rectangle_widget = RectangleWidget()

        # Add the rectangle widget to the layout
        hbox_layout.addWidget(button)
        hbox_layout.addWidget(rectangle_widget)

        # Set the layout to the central widget
        central_widget.setLayout(hbox_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.resize(600, 400)  # Set the initial size of the main window
    main_window.show()

    sys.exit(app.exec())
