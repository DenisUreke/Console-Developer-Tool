from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, QCheckBox
from Models.tile_data_model import TileData

class TileDataView(QWidget):
    def __init__ (self):
        super().__init__()
        
        '''self.tile_data: dict[tuple[int, int], TileData] = {}
        
        layout = QFormLayout()
        layout.addRow("index:", QLabel(str(tile_data.index)))
        layout.addRow("Tileset:", QLabel(tile_data.tileset))
        layout.addRow("Layer:", QLabel(tile_data.layer))
        
        # Walkable
        walkable_label = QCheckBox()
        walkable_label.setChecked(tile_data.walkable)
        walkable_label.setEnabled(False)
        layout.addRow("Walkable:", QLabel(walkable_label))
        
        # Collision
        for side in ["top", "bottom", "left", "right"]:
            cb = QCheckBox()
            cb.setChecked(tile_data.collision[side])
            cb.setEnabled(False)
            layout.addRow(f"Collision {side}:", cb)

        self.setLayout(layout)'''
        
        
        
        
        
        
        
        