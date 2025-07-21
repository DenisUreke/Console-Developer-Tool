from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QFileDialog, QScrollArea, QVBoxLayout
from Models.setup_model import SetupModel
from PySide6.QtGui import QPainter, QPen, QColor, QPixmap
from PySide6.QtCore import Qt, QRect
import os


class TileLabel(QLabel):
    def __init__(self, tile_name, pixmap, tile_index, selector, parent=None):
        super().__init__(parent)
        self.selector = selector
        self.tile_index = tile_index
        self.tile_name = tile_name
        self.selected = False
        self.setPixmap(pixmap)
        self.setFixedSize(pixmap.width(), pixmap.height())

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.parent().parent().mousePressEvent(event)
        elif event.button() == Qt.LeftButton:
            self.selector.tile_selected(self.tile_index, self.tile_name)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MiddleButton:
            self.parent().parent().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.parent().parent().mouseReleaseEvent(event)


    def paintEvent(self, event):
        super().paintEvent(event)

        if self.selected:
            painter = QPainter(self)
            pen = QPen(QColor("red"), 3)
            painter.setPen(pen)
            painter.drawRect(0, 0, self.width()-1, self.height()-1)



'''Create a list of TileLabels, each holding a slce of the tileset'''
class TileSelector(QWidget):
    def __init__(self, model: SetupModel = None):
        super().__init__()
        self.model = model
        self.selected_index = None
        self.selected_name = None
        self.tiles = []

        layout = QVBoxLayout(self) # vertical box like Vstack
        self.container = QWidget() # container for the grid
        self.grid = QGridLayout(self.container) # creates a grid manager for the container
        self.grid.setSpacing(1)

        layout.addWidget(self.container) # the scroll area is added to the main layout

        self.load_tileset_dialog()

    def load_tileset_dialog(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Tileset", "", "Images (*.png *.jpg)")
        name = os.path.basename(path)
        self.model.add_map_to_dictionary(name)
        
        if path:
            self.load_tileset(path, name)

    def load_tileset(self, path, name):
        tileset = QPixmap(path)
        width = tileset.width()
        height = tileset.height()
        
            # --- Clear old tileset ---
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        self.tiles.clear()
        self.selected_index = None
        self.selected_name = None

        columns = width // self.model.tile_size_x
        rows = height // self.model.tile_size_y

        index = 0
        for y in range(rows):
            for x in range(columns):
                # sets the starting point and size of the rectangle
                rect = QRect(x * self.model.tile_size_x, y * self.model.tile_size_y, self.model.tile_size_x, self.model.tile_size_y)
                tile_pixmap = tileset.copy(rect) # slices that specific part out from the tileset
                tile = TileLabel(tile_name=name, pixmap=tile_pixmap, tile_index=index, selector=self)
                self.grid.addWidget(tile, y, x) # adds the tile to the grid layout at specific position
                self.tiles.append(tile)
                index += 1

    def tile_selected(self, index, name):
        print(f"Selected tile: {index}")

        # Unhighlight previously selected tile
        if self.selected_index is not None:
            self.tiles[self.selected_index].selected = False
            self.tiles[self.selected_index].update()

        # Highlight new tile
        self.selected_index = index
        self.selected_name = name
        self.tiles[index].selected = True
        self.tiles[index].update()
