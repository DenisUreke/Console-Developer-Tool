from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout
from Models.main_data_model import mainDataModel
from Draw_Box.lower_tile_layer_view import LowerTileLayerView
from Draw_Box.middle_tile_layer_view import MiddleTileLayerView
from Draw_Box.upper_tile_layer_view import UpperTileLayerView
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QRect
from typing import TYPE_CHECKING

class MapCanvas(QWidget):
    def __init__(self, tile_selector, tile_data_view, model: mainDataModel = None):
        super().__init__()
        self.tile_selector = tile_selector
        self.model = model
        self.tile_data_view = tile_data_view
        self.lower_tile_layer = LowerTileLayerView(self.tile_selector, self.model, parent=self)
        self.middle_tile_layer = MiddleTileLayerView(self.tile_selector, self.model, parent=self)
        self.upper_tile_layer = UpperTileLayerView(self.tile_selector, self.model, parent=self)
        
        
        self.lower_tile_layer.move(0, 0)
        self.lower_tile_layer.raise_()
        self.middle_tile_layer.move(0, 0)
        self.middle_tile_layer.raise_()
        self.upper_tile_layer.move(0, 0)
        self.upper_tile_layer.raise_()
        
        tile_width = self.model.setup_data_model.grid_width * self.model.setup_data_model.tile_size_x
        tile_height = self.model.setup_data_model.grid_height * self.model.setup_data_model.tile_size_y

        self.lower_tile_layer.setFixedSize(tile_width, tile_height)
        self.middle_tile_layer.setFixedSize(tile_width, tile_height)
        self.upper_tile_layer.setFixedSize(tile_width, tile_height)
        
        # mapping for more layers
        self.layer_views = {
            "lower": self.lower_tile_layer,
            "middle": self.middle_tile_layer,
            "upper": self.upper_tile_layer
        }
        
        # Grid to hold tile indices (or None)
        self.setFixedSize(self.model.setup_data_model.grid_width * self.model.setup_data_model.tile_size_x, self.model.setup_data_model.grid_height * self.model.setup_data_model.tile_size_y)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.parent().mousePressEvent(event)
            return
        
        if event.button() == Qt.RightButton:
            x = int(event.position().x() // self.model.setup_data_model.tile_size_x)
            y = int(event.position().y() // self.model.setup_data_model.tile_size_y)

            if 0 <= x < self.model.setup_data_model.grid_width and 0 <= y < self.model.setup_data_model.grid_height:
                tile_data = self.model.tile_dictionary.get((x, y), {}).get(self.model.active_layer)
        
                if tile_data:
                    self.tile_data_view.load_tile_data(tile_data)

                    if tile_data.index is not None and 0 <= tile_data.index < len(self.tile_selector.tiles):
                        if self.tile_selector.selected_index is not None:
                            self.tile_selector.tiles[self.tile_selector.selected_index].selected = False
                            self.tile_selector.tiles[self.tile_selector.selected_index].update()

                        self.tile_selector.selected_index = tile_data.index
                        self.tile_selector.tiles[tile_data.index].selected = True
                        self.tile_selector.tiles[tile_data.index].update()


        if event.button() == Qt.LeftButton:
            x = int(event.position().x() // self.model.setup_data_model.tile_size_x)
            y = int(event.position().y() // self.model.setup_data_model.tile_size_y)

            if 0 <= x < self.model.setup_data_model.grid_width and 0 <= y < self.model.setup_data_model.grid_height:
                index = self.tile_selector.selected_index
                if index is not None:
                    tile_data = self.model.tile_dictionary.get((x, y), {}).get(self.model.active_layer)
                    if tile_data:
                        tile_data.index = index
                    self.layer_views[self.model.active_layer].update()

                tile_data = self.model.tile_dictionary.get((x, y))
                if tile_data:
                    self.tile_data_view.load_tile_data(tile_data)


    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.RightButton:
            self.parent().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.RightButton:
            self.parent().mouseReleaseEvent(event)

