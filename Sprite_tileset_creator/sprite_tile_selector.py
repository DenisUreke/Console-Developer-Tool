from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QFileDialog, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor
from Sprite_tileset_creator.sprite_data_model import SpriteDataModel
import os

class SpriteTileLabel(QLabel):
    def __init__(self, tile_name, pixmap, tile_index, selector, parent=None):
        super().__init__(parent)
        self.selector = selector
        self.tile_index = tile_index
        self.tile_name = tile_name
        self.selected = False
        self.setPixmap(pixmap)
        self.setFixedSize(pixmap.width(), pixmap.height())
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.selector.tile_selected(self.tile_index, self.tile_name)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        
        if self.selected:
            painter = QPainter(self)
            pen = QPen(QColor("red"), 3)
            painter.setPen(pen)
            painter.drawRect(0,0,self.width()-1, self.height()-1)
            
class SpriteTileSelector(QWidget):
    def __init__(self, model: SpriteDataModel = None):
        super().__init__()
        
        self.model = model
        self.selected_index = None
        self.selected_name = None
        self.tiles = []
        
        layout = QVBoxLayout(self)
        
        # --- TileSet Toggle Buttons ---
        self.toggle_button_bar = QHBoxLayout()
        self.toggle_buttons = {}  # Optional: keep references if needed
        layout.addLayout(self.toggle_button_bar)  # Add button bar at the top
        
        # --- TileGrid Container ---
        self.container = QWidget()
        self.grid = QGridLayout(self.container)
        self.grid.setSpacing(1)
        layout.addWidget(self.container)
        
    def load_tileset_dialog(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Tileset", "", "images (*.png *.jpg)")
        if path:
            name = os.path.basename(path)
            self.model.load_tileset(name, path)
            self.display_active_tileset(name)
            self.refresh_tileset_buttons()
    
    def display_active_tileset(self, name):
        self.model.active_tileset_name = name
        
        # Clear the current tile grid
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)
                
        self.tiles.clear()
        self.selected_index = None
        self.selected_name = None
        
        # Get the original tileset image to calculate layout
        full_image = self.model.tileset_images.get(name)
        if not full_image:
            return
        
        tile_width = self.model.tile_size_x
        tile_height = self.model.tile_size_y
        image_width = full_image.width()
        image_height = full_image.height()
        
        columns = image_width // tile_width
        
        for index, tile_pixmap in enumerate(self.model.tilesets[name]):
            row = index // columns
            col = index % columns
            
            tile = SpriteTileLabel(tile_name=name, pixmap=tile_pixmap, tile_index=index, selector= self)
            self.grid.addWidget(tile, row, col)
            self.tiles.append(tile)
            
    def tile_selected(self, index, name):
        
        # Unhighlight previously selected tile
        if self.selected_index is not None:
            self.tiles[self.selected_index].selected = False
            self.tiles[self.selected_index].update()
         
        # Highlight new tile   
        self.selected_index = index
        self.selected_name = name
        self.tiles[index].selected = True
        self.tiles[index].update()

    def refresh_tileset_buttons(self):
        while self.toggle_button_bar.count():
            item = self.toggle_button_bar.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        tile_index = 1
        for name in self.model.tilesets.keys():
            button = QPushButton(f"{tile_index}")
            button.setCheckable(True)
            button.setMaximumWidth(30)
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.clicked.connect(lambda _, n=name: self.set_active_tileset(n))
            self.toggle_button_bar.addWidget(button, alignment=Qt.AlignLeft)
            self.toggle_buttons[name] = button
            tile_index += 1
            
        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.toggle_button_bar.addItem(spacer)

            
    def set_active_tileset(self, name):
        # Display tileset
        self.display_active_tileset(name)

        # Update button checked state
        for n, btn in self.toggle_buttons.items():
            btn.setChecked(n == name)
            
        
        