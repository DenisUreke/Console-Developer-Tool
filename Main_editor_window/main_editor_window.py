from PySide6.QtWidgets import QWidget, QHBoxLayout
from Models.setup_model import SetupModel
from Models.tile_data_model import TileData
from Tile_data_view.tile_data_view import TileDataView
from Tile_selector.tile_selector import TileSelector
from Map_canvas.map_canvas import MapCanvas

class MainEditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tile Map Editor")
        self.setup_model = SetupModel()
        self.tile_data = TileData()
        self.tile_data_view = TileDataView(self.tile_data)

        self.tile_selector = TileSelector(model=self.setup_model)
        self.canvas = MapCanvas(self.tile_selector, model=self.setup_model)

        layout = QHBoxLayout(self)
        layout.addWidget(self.tile_selector)
        layout.addWidget(self.canvas)
