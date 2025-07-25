# sprite_tileset_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea
from Sprite_tileset_creator.sprite_data_model import SpriteDataModel
from Sprite_tileset_creator.sprite_tile_selector import SpriteTileSelector
from Sprite_tileset_creator.sprite_tile_canvas import SpriteCanvas
from Sprite_tileset_creator.sprite_controls import SpriteControls

class SpriteTilesetWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sprite Tile‑Set Creator")

        # 1) Shared model
        self.model = SpriteDataModel()

        # 2) Left and right views
        self.selector = SpriteTileSelector(self.model)
        self.canvas   = SpriteCanvas(self.selector, self.model)

        # wrap each in a scroll‑area
        self.selector_area = QScrollArea()
        self.selector_area.setWidgetResizable(True)
        self.selector_area.setWidget(self.selector)
        self.selector_area.setFixedSize(700, 600)

        self.canvas_area = QScrollArea()
        self.canvas_area.setWidgetResizable(True)
        self.canvas_area.setWidget(self.canvas)
        self.canvas_area.setFixedSize(500, 600)

        # 3) Controls bar at the top
        self.controls = SpriteControls(self.model, self.selector, self.canvas)

        # 4) Put it all together
        container = QWidget()
        self.setCentralWidget(container)
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(5,5,5,5)
        main_layout.setSpacing(4)

        main_layout.addWidget(self.controls)       # ← top bar
        h = QHBoxLayout()                          # ← bottom two panels
        h.addWidget(self.selector_area)
        h.addWidget(self.canvas_area)
        main_layout.addLayout(h)

        # optional: menus or toolbars
        self._create_menus()

    def _create_menus(self):
        file = self.menuBar().addMenu("&File")
        file.addAction("Exit", self.close)
