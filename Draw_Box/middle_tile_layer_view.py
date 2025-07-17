from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QRect
from Models.main_data_model import mainDataModel

class MiddleTileLayerView(QWidget):
    def __init__(self, tile_selector, model: mainDataModel, parent=None):
        super().__init__(parent)
        self.tile_selector = tile_selector
        self.model = model
        self.grid = model.grid
        
        
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setFixedHeight(900)
        self.setFixedWidth(965)
        
    def paintEvent(self, event):
        painter = QPainter(self)

        for y in range(self.model.setup_data_model.grid_height):
            for x in range(self.model.setup_data_model.grid_width):
                tile_index = self.grid[y][x]
                if tile_index is not None:
                    tile_pixmap = self.tile_selector.tiles[tile_index].pixmap()
                    painter.drawPixmap(
                        x * self.model.setup_data_model.tile_size_x,
                        y * self.model.setup_data_model.tile_size_y,
                        tile_pixmap
                    )

                painter.setPen(Qt.gray)
                painter.drawRect(
                    x * self.model.setup_data_model.tile_size_x,
                    y * self.model.setup_data_model.tile_size_y,
                    self.model.setup_data_model.tile_size_x,
                    self.model.setup_data_model.tile_size_y
                )
