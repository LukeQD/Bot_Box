from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt, QPointF, QPoint
import math

class position_widget(QWidget):
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

        self.theta_base = 0
        self.base_position = QPointF(self.width() // 2, self.height()-600)
        self.base_radius = 50
        self.base_joint = self.calculate_joint(self.base_position, self.base_radius, self.theta_base)

        self.Joints = "j1"  # Can be "j1" or "j2"
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
        pen = QPen(Qt.black, 8)
        painter.setPen(pen)

        # Draw links
        self.joint1 = self.calculate_joint(self.base, self.link1_length, self.angle1)
        self.joint2 = self.calculate_joint(self.joint1, self.link2_length, self.angle2)
        painter.drawLine(self.base, self.joint1)
        painter.drawLine(self.joint1, self.joint2)

        painter.drawEllipse(self.base_position, self.base_radius, self.base_radius)
        self.base_joint = self.calculate_joint(self.base_position, self.base_radius, self.theta_base)
        painter.drawLine(self.base_position, self.base_joint)

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
                print("J1")
                self.angle1 = self.calculate_angle(self.base, mouse_pos)
            elif self.Joints == "j2":
                print("J2")
                self.angle2 = self.calculate_angle(self.joint1, mouse_pos)
            elif self.Joints == "j0":
                self.theta_base = self.calculate_angle(self.base_position, mouse_pos)
                print(self.theta_base)
            self.update()

    def mouseReleaseEvent(self, event):
        """Stop dragging."""
        self.dragging = False

    def calculate_angle(self, origin, target):
        """Calculate the angle between the origin and the target in degrees."""
        dx = target.x() - origin.x()
        dy = origin.y() - target.y()
        return math.degrees(math.atan2(dy, dx))

    
    def resizeEvent(self, event):
        # Update the anchor point (bottom center of the window)
        #link 1:
        self.base = QPointF(self.width() // 2, self.height()-100)
        self.base_position = QPointF(self.width() // 2, self.height()-600)
        self.joint1 = self.calculate_joint(self.base, self.link1_length, self.angle1)
        self.joint2 = self.calculate_joint(self.joint1, self.link2_length, self.angle2)
        self.base_joint = self.calculate_joint(self.base_position, self.base_radius, self.theta_base)
        self.update()  # Redraw the widget when the window is resized
        super().resizeEvent(event)  # Call the base class implementation

    def set_joint(self, index):
        if index == 0:
            self.Joints = "j0"
        elif index == 1:
            self.Joints = "j1"
        else:
            self.Joints = "j2"
        
    def get_position(self):
        J1 = self.angle1
        J2 = self.angle2

        #adjust Joint 2
        if J2 < 180 and J2 > 0:
            J2 -= J1
        elif J1 > 90:
            J2 = -J2
            J2 = 180 - J1 + (180 - J2)
        else:
            J2 -= J1
        J2 += 90

        #check if J2 is out of range
        if J2 > 180:
            J2 = 180
        elif J2 < 0:
            J2 = 0
        
        #check if J1 is out of range:
        if J1 > 180:
            J1 = 180
        elif J1 < 0:
            J1 = 0
        
        base_pos = self.theta_base
        if base_pos < 0:
            base_pos = 360 + base_pos

        return J1, base_pos, J2
    