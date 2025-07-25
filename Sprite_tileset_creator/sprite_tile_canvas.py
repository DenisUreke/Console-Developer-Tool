from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent, QColor
from PySide6.QtCore import Qt, QRect, QSize
from collections import defaultdict
from Sprite_tileset_creator.sprite_data_model import SpriteDataModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Sprite_tileset_creator.sprite_tile_selector import SpriteTileSelector
    

class SpriteCanvas(QWidget):
    def __init__(self, sprite_tile_selector: 'SpriteTileSelector', model: SpriteDataModel):
        super().__init__()
        self.tile_selector = sprite_tile_selector
        self.model = model

        self.setMinimumSize(self.sizeHint())
        
        self.get_text = defaultdict(
            lambda: "Unknown movement",
            {
                0: "Moving up",
                1: "Moving up‑right",
                2: "Moving right",
                3: "Moving down‑right",
                4: "Moving down",
                5: "Moving down‑left",
                6: "Moving left",
                7: "Moving up‑left",
                8: "Attack 1",
                9: "Attack 2",
                10: "Attack 3",
                11: "Death",
                12: "Climb",
                13: "Idle",
                14: "Run",
                15: "Jump",
                16: "Push",
                17: "Object animation"
            }
        )
   
    def sizeHint(self) -> QSize:
       # total pixel size = tile_size × grid dimensions
       return QSize(
           self.model.grid_width  * self.model.tile_size_x, self.model.grid_height * self.model.tile_size_y
       )
        
    def mousePressEvent(self, event: QMouseEvent):
        
        tile_x = event.x() // self.model.tile_size_x
        tile_y = event.y() // self.model.tile_size_y
        
        if event.button() == Qt.LeftButton:

            if (0 <= tile_x < self.model.grid_width) and (0 <= tile_y < self.model.grid_height):
                if self.tile_selector.selected_name is not None:
                    tile_info = (self.tile_selector.selected_name, self.tile_selector.selected_index)
                    self.model.grid[tile_y][tile_x] = tile_info
                    self.update()
                    
        elif event.button() == Qt.RightButton:
            self.model.grid[tile_y][tile_x] = None
            self.update()
                
    def paintEvent(self, event):
        painter = QPainter(self)
        tile_w = self.model.tile_size_x
        tile_h = self.model.tile_size_y

        # 1) Draw all the tiles
        for y in range(self.model.grid_height):
            for x in range(self.model.grid_width):
                info = self.model.grid[y][x]
                if info:
                    name, idx = info
                    painter.drawPixmap(x*tile_w, y*tile_h,
                                       self.model.tilesets[name][idx])

        # 2) Draw the grid lines
        pen = painter.pen()
        pen.setColor(Qt.gray)
        painter.setPen(pen)
        for x in range(self.model.grid_width+1):
            painter.drawLine(x*tile_w, 0,
                             x*tile_w, self.model.grid_height*tile_h)
        for y in range(self.model.grid_height+1):
            painter.drawLine(0, y*tile_h,
                             self.model.grid_width*tile_w, y*tile_h)

        # 3) Draw one label *per row*, immediately to the right of that row
        painter.setPen(Qt.white)
        fm = painter.fontMetrics()
        margin = 8  # pixels between your grid and the text

        for y in range(self.model.grid_height):
            text = self.get_text[y]
            tw = fm.horizontalAdvance(text)
            th = fm.ascent()
            # X position: just past the right edge of the grid
            x_pos = self.model.grid_width * tile_w + margin
            # Y position: vertically centered in that row
            y_pos = y*tile_h + (tile_h + th)//2
            painter.drawText(x_pos, y_pos, text)

        
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
    
    def sizeHint(self) -> QSize:
        return QSize(
            self.model.grid_width * self.model.tile_size_x,
            self.model.grid_height * self.model.tile_size_y
        )

