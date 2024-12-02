from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt, QPointF
import math

class RobotArmWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot Arm Control")
        self.setGeometry(100, 100, 600, 400)

        # Initial configuration
        self.link1_length = 150
        self.link2_length = 100
        self.angle1 = 0  # Angle of link1 in degrees
        self.angle2 = 0  # Angle of link2 in degrees

        self.base = QPointF(300, 300)  # Base position (P0)
        self.joint1 = self.calculate_joint(self.base, self.link1_length, self.angle1)
        self.joint2 = self.calculate_joint(self.joint1, self.link2_length, self.angle2)

        self.Joints = "j2"  # Can be "j1" or "j2"
        self.dragging = False

    def calculate_joint(self, origin, length, angle):
        """Calculate the endpoint of a link based on origin, length, and angle."""
        rad_angle = math.radians(angle)
        x = origin.x() + length * math.cos(rad_angle)
        y = origin.y() - length * math.sin(rad_angle)
        return QPointF(x, y)

    def paintEvent(self, event):
        """Draw the robot arm."""
        painter = QPainter(self)
        pen = QPen(Qt.black, 3)
        painter.setPen(pen)

        # Draw links
        self.joint1 = self.calculate_joint(self.base, self.link1_length, self.angle1)
        self.joint2 = self.calculate_joint(self.joint1, self.link2_length, self.angle2)
        painter.drawLine(self.base, self.joint1)
        painter.drawLine(self.joint1, self.joint2)
        painter.end()

    def mousePressEvent(self, event):
        """Start dragging based on the active joint."""
        mouse_pos = event.pos()
        self.dragging = True

    def mouseMoveEvent(self, event):
        """Update the angle of the active joint while dragging."""
        mouse_pos = event.pos()
        if self.dragging:
            if self.Joints == "j1":
                self.angle1 = self.calculate_angle(self.base, mouse_pos)
            elif self.Joints == "j2":
                self.angle2 = self.calculate_angle(self.joint1, mouse_pos)
            self.update()

    def mouseReleaseEvent(self, event):
        """Stop dragging."""
        self.dragging = False

    def calculate_angle(self, origin, target):
        """Calculate the angle between the origin and the target in degrees."""
        dx = target.x() - origin.x()
        dy = origin.y() - target.y()
        return math.degrees(math.atan2(dy, dx))


if __name__ == "__main__":
    app = QApplication([])
    widget = RobotArmWidget()
    widget.show()
    app.exec()
