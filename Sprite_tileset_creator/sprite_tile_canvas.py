from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QRect
import copy
from Sprite_tileset_creator.sprite_data_model import SpriteDataModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Sprite_tileset_creator.sprite_tile_selector import SpriteTileSelector
    

class SpriteCanvas(QWidget):
    def __init__(self, sprite_tile_selector: 'SpriteTileSelector', model: SpriteDataModel):
        super().__init__()
        self.tile_selector = sprite_tile_selector
        self.model = model
        
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            tile_x = event.x() // self.model.tile_size_x
            tile_y = event.y() // self.model.tile_size_y

            if (0 <= tile_x < self.model.grid_width) and (0 <= tile_y < self.model.grid_height):
                if self.tile_selector.selected_name is not None:
                    tile_info = (self.tile_selector.selected_name, self.tile_selector.selected_index)
                    self.model.grid[tile_y][tile_x] = tile_info
                    self.update()
        elif event.button() == Qt.RightButton:
            self.grid[tile_y][tile_x] = None
            self.update()
                
    def paintEvent(self, event):
        painter = QPainter(self)
        tile_w = self.model.tile_size_x
        tile_h = self.model.tile_size_y

        for y in range(self.model.grid_height):
            for x in range(self.model.grid_width):
                tile_info = self.model.grid[y][x]
                if tile_info:
                    name, index = tile_info
                    pixmap = self.model.tilesets[name][index]
                    painter.drawPixmap(x * tile_w, y * tile_h, pixmap)

        # Optional: draw grid
        pen = painter.pen()
        pen.setColor(Qt.gray)
        painter.setPen(pen)
        for x in range(self.model.grid_width + 1):
            painter.drawLine(x * tile_w, 0, x * tile_w, self.model.grid_height * tile_h)
        for y in range(self.model.grid_height + 1):
            painter.drawLine(0, y * tile_h, self.model.grid_width * tile_w, y * tile_h)
        
    def export_as_image(self, path: str):
        tile_w = self.model.tile_size_x
        tile_h = self.model.tile_size_y
        canvas = QPixmap(tile_w * self.model.grid_width, tile_h * self.model.grid_height)
        canvas.fill(Qt.transparent)

        painter = QPainter(canvas)
        for y in range(self.model.grid_height):
            for x in range(self.model.grid_width):
                tile_info = self.model.grid[y][x]
                if tile_info:
                    name, index = tile_info
                    pixmap = self.model.tilesets[name][index]
                    painter.drawPixmap(x * tile_w, y * tile_h, pixmap)
        painter.end()

        canvas.save(path)

