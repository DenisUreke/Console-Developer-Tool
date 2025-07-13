from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QFileDialog, QScrollArea, QVBoxLayout
from PySide6.QtGui import QPixmap, QPainter, QPen
from PySide6.QtCore import Qt, QRect


class TileLabel(QLabel):
    def __init__(self, pixmap, tile_index, selector, parent=None):
        super().__init__(parent)
        self.selector = selector  # Store reference to TileSelector
        self.tile_index = tile_index
        self.setPixmap(pixmap)
        self.setFixedSize(pixmap.width(), pixmap.height())

    def mousePressEvent(self, event):
        self.selector.tile_selected(self.tile_index)


class TileSelector(QWidget):
    def __init__(self, tile_size=100):
        super().__init__()
        self.tile_size = tile_size
        self.selected_index = None
        self.tiles = []

        layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea()
        self.container = QWidget()
        self.grid = QGridLayout(self.container)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.container)
        layout.addWidget(self.scroll_area)

        self.load_tileset_dialog()

    def load_tileset_dialog(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Tileset", "", "Images (*.png *.jpg)")
        if path:
            self.load_tileset(path)

    def load_tileset(self, path):
        tileset = QPixmap(path)
        width = tileset.width()
        height = tileset.height()

        columns = width // self.tile_size
        rows = height // self.tile_size

        index = 0
        for y in range(rows):
            for x in range(columns):
                rect = QRect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                tile_pixmap = tileset.copy(rect)
                tile = TileLabel(tile_pixmap, index, self)
                self.grid.addWidget(tile, y, x)
                self.tiles.append(tile)
                index += 1

    def tile_selected(self, index):
        print(f"Selected tile: {index}")
        self.selected_index = index
        # You can emit a signal here or call a callback
