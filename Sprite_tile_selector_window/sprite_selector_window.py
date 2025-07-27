# sprite_tileset_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea
from Models.setup_model import SetupModel
from Sprite_tile_selector_window.sprite_selector import SpriteTileSelectorMain
from Sprite_tileset_creator.sprite_controls import SpriteControls

class SpriteTilesetWindowMain(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sprite Tile‑Set Creator")

        # 1) Shared model
        self.model = SetupModel()

        # 2) Left and right views
        self.selector = SpriteTileSelectorMain(self.model)

        # wrap each in a scroll‑area
        self.selector_area = QScrollArea()
        self.selector_area.setWidgetResizable(True)
        self.selector_area.setWidget(self.selector)
        self.selector_area.setFixedSize(700, 600)
        
        # 3) Controls bar at the top
        self.controls = SpriteControls(self.selector)

        # 4) Put it all together
        container = QWidget()
        self.setCentralWidget(container)
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(5,5,5,5)
        main_layout.setSpacing(4)

        main_layout.addWidget(self.controls)       # ← top bar
        h = QHBoxLayout()                          # ← bottom two panels
        h.addWidget(self.selector_area)
        main_layout.addLayout(h)

        # optional: menus or toolbars
        self._create_menus()

    def _create_menus(self):
        file = self.menuBar().addMenu("&File")
        file.addAction("Exit", self.close)
        
