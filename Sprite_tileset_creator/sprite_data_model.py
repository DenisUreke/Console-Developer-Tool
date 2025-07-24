from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect

class SpriteDataModel:
    def __init__(self):
        
        self.tile_size_x: int = 32
        self.tile_size_y: int = 32
        self.grid_width: int = 58
        self.grid_height: int = 46
         
        self.active_tileset_name: str = ""
        self.tilesets: dict[str, list[QPixmap]] = {}
        self.tileset_images: dict[str, QPixmap] = {}
        
        self.grid = [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]

        