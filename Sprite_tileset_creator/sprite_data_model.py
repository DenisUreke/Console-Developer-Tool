from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect

class SpriteDataModel:
    def __init__(self):
        
        self.tile_size_x: int = 32
        self.tile_size_y: int = 32
        self.grid_width: int = 6
        self.grid_height: int = 15
         
        self.active_tileset_name: str = ""
        self.tilesets: dict[str, list[QPixmap]] = {}
        self.tileset_images: dict[str, QPixmap] = {}
        
        self.grid = [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        
    def load_tileset(self, name: str, image_path: str):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            raise ValueError(f"Failed to load image: {image_path}")
    
        self.tileset_images[name] = pixmap
        sliced = []
    
        tile_width = self.tile_size_x
        tile_height = self.tile_size_y
        rows = pixmap.height() // tile_height
        cols = pixmap.width() // tile_width
    
        for y in range(rows):
            for x in range(cols):
                rect = QRect(x * tile_width, y * tile_height, tile_width, tile_height)
                tile = pixmap.copy(rect)
                sliced.append(tile)
    
        self.tilesets[name] = sliced

        if not self.active_tileset_name:
            self.active_tileset_name = name

        