from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout
from Models.main_data_model import mainDataModel
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QRect
from typing import TYPE_CHECKING

class MapCanvas(QWidget):
    def __init__(self, tile_selector, tile_data_view, model: mainDataModel = None):
        super().__init__()
        self.tile_selector = tile_selector
        self.model = model
        self.tile_data_view = tile_data_view
        
        # Grid to hold tile indices (or None)
        self.grid = [[None for _ in range(self.model.setup_data_model.grid_width)] for _ in range(self.model.setup_data_model.grid_height)] # Create matrix of None values
        self.setFixedSize(self.model.setup_data_model.grid_width * self.model.setup_data_model.tile_size_x, self.model.setup_data_model.grid_height * self.model.setup_data_model.tile_size_y)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw the grid and placed tiles
        for y in range(self.model.setup_data_model.grid_height):
            for x in range(self.model.setup_data_model.grid_width):
                tile_index = self.grid[y][x]
                if tile_index is not None:
                    tile_pixmap = self.tile_selector.tiles[tile_index].pixmap()
                    # Draw the tile at the grid position top left corner is x,y
                    painter.drawPixmap(x * self.model.setup_data_model.tile_size_x, y * self.model.setup_data_model.tile_size_y, tile_pixmap) 

                # Draw grid lines
                painter.setPen(Qt.gray)
                painter.drawRect(x * self.model.setup_data_model.tile_size_x, y * self.model.setup_data_model.tile_size_y, self.model.setup_data_model.tile_size_x, self.model.setup_data_model.tile_size_y)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.parent().mousePressEvent(event)
            return
        
        if event.button() == Qt.RightButton:
            x = int(event.position().x() // self.model.setup_data_model.tile_size_x)
            y = int(event.position().y() // self.model.setup_data_model.tile_size_y)

            if 0 <= x < self.model.setup_data_model.grid_width and 0 <= y < self.model.setup_data_model.grid_height:
                tile_data = self.model.tile_dictionary.get((x, y))
                if tile_data:
                    # ✅ Show data in the TileDataView
                    self.tile_data_view.load_tile_data(tile_data)

                    # ✅ Also highlight it in the TileSelector
                    if tile_data.index is not None and 0 <= tile_data.index < len(self.tile_selector.tiles):
                        # Unhighlight previous
                        if self.tile_selector.selected_index is not None:
                            self.tile_selector.tiles[self.tile_selector.selected_index].selected = False
                            self.tile_selector.tiles[self.tile_selector.selected_index].update()

                        self.tile_selector.selected_index = tile_data.index
                        self.tile_selector.tiles[tile_data.index].selected = True
                        self.tile_selector.tiles[tile_data.index].update()

        if event.button() == Qt.LeftButton:
            x = int(event.position().x() // self.model.setup_data_model.tile_size_x)
            y = int(event.position().y() // self.model.setup_data_model.tile_size_y)

            if 0 <= x < self.model.setup_data_model.grid_width and 0 <= y < self.model.setup_data_model.grid_height:
                index = self.tile_selector.selected_index
                if index is not None:
                    self.grid[y][x] = index
                    tile_data = self.model.tile_dictionary.get((x, y))
                    if tile_data:
                        tile_data.index = index
                    self.update()

                tile_data = self.model.tile_dictionary.get((x, y))
                if tile_data:
                    self.tile_data_view.load_tile_data(tile_data)


    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.RightButton:
            self.parent().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.RightButton:
            self.parent().mouseReleaseEvent(event)

