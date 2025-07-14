from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QFileDialog, QScrollArea, QVBoxLayout
from Models.setup_model import SetupModel
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


'''Create a list of TileLabels, each holding a slce of the tileset'''
class TileSelector(QWidget):
    def __init__(self, model: SetupModel = None):
        super().__init__()
        self.model = model
        self.selected_index = None
        self.tiles = []

        layout = QVBoxLayout(self) # vertical box like Vstack

        self.scroll_area = QScrollArea() #scrollable area
        self.container = QWidget() # container for the grid
        self.grid = QGridLayout(self.container) # creates a grid manager for the container
        self.grid.setSpacing(1)

        self.scroll_area.setWidgetResizable(True) # for resizing the scroll area
        self.scroll_area.setWidget(self.container) # the container is added to the scroll area
        layout.addWidget(self.scroll_area) # the scroll area is added to the main layout

        self.load_tileset_dialog()

    def load_tileset_dialog(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Tileset", "", "Images (*.png *.jpg)")
        if path:
            self.load_tileset(path)

    def load_tileset(self, path):
        tileset = QPixmap(path)
        width = tileset.width()
        height = tileset.height()

        columns = width // self.model.tile_size_x
        rows = height // self.model.tile_size_y

        index = 0
        for y in range(rows):
            for x in range(columns):
                # sets the starting point and size of the rectangle
                rect = QRect(x * self.model.tile_size_x, y * self.model.tile_size_y, self.model.tile_size_x, self.model.tile_size_y)
                tile_pixmap = tileset.copy(rect) # slices that specific part out from the tileset
                tile = TileLabel(tile_pixmap, index, self)
                self.grid.addWidget(tile, y, x) # adds the tile to the grid layout at specific position
                self.tiles.append(tile)
                index += 1

    def tile_selected(self, index):
        print(f"Selected tile: {index}")
        self.selected_index = index
        # You can emit a signal here or call a callback
