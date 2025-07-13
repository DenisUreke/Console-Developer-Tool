from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QRect

class MapCanvas(QWidget):
    def __init__(self, tile_selector, grid_width=30, grid_height=20, tile_size=32):
        super().__init__()
        self.tile_selector = tile_selector
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.tile_size = tile_size

        # Grid to hold tile indices (or None)
        self.grid = [[None for _ in range(grid_width)] for _ in range(grid_height)]
        self.setFixedSize(grid_width * tile_size, grid_height * tile_size)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw the grid and placed tiles
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                tile_index = self.grid[y][x]
                if tile_index is not None:
                    tile_pixmap = self.tile_selector.tiles[tile_index].pixmap()
                    painter.drawPixmap(x * self.tile_size, y * self.tile_size, tile_pixmap)

                # Draw grid lines
                painter.setPen(Qt.gray)
                painter.drawRect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            x = event.position().x() // self.tile_size
            y = event.position().y() // self.tile_size

            if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
                index = self.tile_selector.selected_index
                if index is not None:
                    self.grid[int(y)][int(x)] = index
                    self.update()
