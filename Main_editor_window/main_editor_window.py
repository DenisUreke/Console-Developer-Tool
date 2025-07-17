# main_editor_window.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QScrollArea
from Models.setup_model import SetupModel
from Models.main_data_model import mainDataModel
from Tile_selector.tile_selector import TileSelector
from Map_canvas.map_canvas import MapCanvas
from Tile_Data_Window.tile_data_window import TileDataWindow
from Drag_and_scroll_area.drag_and_scroll_area import DragScrollArea

class MainEditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tile Map Editor")

        self.setup_model = SetupModel()
        self.main_data_model = mainDataModel(self.setup_model)

        self.tile_selector = TileSelector(model=self.setup_model)

        # ✅ Create external tile data window and show it
        self.tile_data_window = TileDataWindow()
        self.tile_data_window.show()

        self.canvas = MapCanvas(
            tile_selector=self.tile_selector,
            tile_data_view=self.tile_data_window.tile_data_view,  # ✅ pass reference to internal view
            model=self.main_data_model
        )
        self.canvas_scroll_area = DragScrollArea()
        self.canvas_scroll_area.setWidgetResizable(True)
        self.canvas_scroll_area.setWidget(self.canvas)
        self.canvas_scroll_area.setFixedHeight(900)
        self.canvas_scroll_area.setFixedWidth(965)

        self.tile_selector_scroll = DragScrollArea()
        self.tile_selector_scroll.setWidgetResizable(True)
        self.tile_selector_scroll.setWidget(self.tile_selector)
        self.tile_selector_scroll.setFixedHeight(900)
        self.tile_selector_scroll.setFixedWidth(635)

        layout = QHBoxLayout(self)
        layout.addWidget(self.tile_selector_scroll, stretch=1)
        layout.addWidget(self.canvas_scroll_area, stretch=1)
