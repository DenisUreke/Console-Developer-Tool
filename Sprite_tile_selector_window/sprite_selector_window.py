from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from Sprite_tile_selector_window.sprite_selector import SpriteTileSelectorMain
from Models.setup_model import SetupModel  # You already use this in SpriteTileSelectorMain
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Models.setup_model import SetupModel

import os

class SpriteTilesetWindowMain(QDialog):
    def __init__(self, model: 'SetupModel', image_path: str, parent=None,):
        super().__init__(parent)
        self.setWindowTitle("Sprite Tileset Viewer")
        self.setMinimumSize(600, 400)

        # --- 1. Create a temporary model just for this popup ---
        self.model = model

        # Set default tile size (change as needed)
        self.model.tile_size_x = 32
        self.model.tile_size_y = 32

        # --- 2. Load the image into the model ---
        name = os.path.basename(image_path)
        self.model.load_tileset(name, image_path)

        # --- 3. Inject the model into the tile selector ---
        self.selector = SpriteTileSelectorMain(model=self.model)
        self.selector.display_active_tileset(name)

        # --- 4. Layout ---
        layout = QVBoxLayout()
        layout.addWidget(self.selector)
        self.setLayout(layout)
