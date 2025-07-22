from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QRect
from Models.main_data_model import MainDataModel

class BackgroundImageLayerView(QWidget):
    def __init__(self, model: MainDataModel, parent=None):
        super().__init__(parent)
        self.model = model
        
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setFixedHeight(900)
        self.setFixedWidth(965)
        
    '''def paintEvent(self, event):
        painter = QPainter(self)
        if isinstance(self.model.background_image_layer, QPixmap):
            painter.drawPixmap(0, 0, self.model.background_image_layer)'''
            
    def paintEvent(self, event):
        painter = QPainter(self)

        if isinstance(self.model.background_image_layer, QPixmap):
            stretched_pixmap = self.model.background_image_layer.scaled(
                self.width(),
                self.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            painter.drawPixmap(0, 0, stretched_pixmap)
        
        