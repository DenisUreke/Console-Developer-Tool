from PySide6.QtWidgets import QWidget, QHBoxLayout
from Tile_selector.tile_selector import TileSelector
from Map_canvas.map_canvas import MapCanvas  # ✅ Make sure this import path is correct

class MainEditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tile Map Editor")

        self.tile_selector = TileSelector(tile_size=32)
        self.canvas = MapCanvas(self.tile_selector, grid_width=30, grid_height=20, tile_size=32)

        layout = QHBoxLayout(self)
        layout.addWidget(self.tile_selector)
        layout.addWidget(self.canvas)
