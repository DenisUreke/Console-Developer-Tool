# tile_data_window.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from Tile_data_view.tile_data_view import TileDataView

class TileDataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tile Data View")
        self.setFixedWidth(250)  # Optional, for consistent sizing

        layout = QVBoxLayout(self)
        self.tile_data_view = TileDataView()
        layout.addWidget(self.tile_data_view)

    def load_tile_data(self, tile_data):
        self.tile_data_view.load_tile_data(tile_data)
