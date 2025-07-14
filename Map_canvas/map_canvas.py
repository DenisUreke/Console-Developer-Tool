from PySide6.QtWidgets import QWidget
from Models.setup_model import SetupModel
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QRect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Tile_selector.tile_selector import TileSelector

class MapCanvas(QWidget):
    def __init__(self, tile_selector: TileSelector, model: SetupModel = None):
        super().__init__()
        self.tile_selector = tile_selector
        self.model = model

        # Grid to hold tile indices (or None)
        self.grid = [[None for _ in range(self.model.grid_width)] for _ in range(self.model.grid_height)] # Create matrix of None values
        self.setFixedSize(self.model.grid_width * self.model.tile_size_x, self.model.grid_height * self.model.tile_size_y)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw the grid and placed tiles
        for y in range(self.model.grid_height):
            for x in range(self.model.grid_width):
                tile_index = self.grid[y][x]
                if tile_index is not None:
                    tile_pixmap = self.tile_selector.tiles[tile_index].pixmap()
                    # Draw the tile at the grid position top left corner is x,y
                    painter.drawPixmap(x * self.model.tile_size_x, y * self.model.tile_size_y, tile_pixmap) 

                # Draw grid lines
                painter.setPen(Qt.gray)
                painter.drawRect(x * self.model.tile_size_x, y * self.model.tile_size_y, self.model.tile_size_x, self.model.tile_size_y)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            x = event.position().x() // self.model.tile_size_x
            y = event.position().y() // self.model.tile_size_y

            if 0 <= x < self.model.grid_width and 0 <= y < self.model.grid_height:
                index = self.tile_selector.selected_index
                if index is not None:
                    self.grid[int(y)][int(x)] = index
                    self.update()
