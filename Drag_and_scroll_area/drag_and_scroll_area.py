from PySide6.QtWidgets import QScrollArea
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent

class DragScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.dragging = False
        self.last_mouse_pos = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.dragging = True
            self.last_mouse_pos = event.globalPosition().toPoint()
            self.setCursor(Qt.ClosedHandCursor)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            current_pos = event.globalPosition().toPoint()
            delta = current_pos - self.last_mouse_pos
            self.last_mouse_pos = current_pos

            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.dragging = False
            self.setCursor(Qt.ArrowCursor)
        super().mouseReleaseEvent(event)
