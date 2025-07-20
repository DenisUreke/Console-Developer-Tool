# main_editor_window.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QScrollArea
from Models.setup_model import SetupModel
from Models.main_data_model import MainDataModel
from Tile_selector.tile_selector import TileSelector
from Map_canvas.map_canvas import MapCanvas
from Tile_Data_Window.tile_data_window import TileDataWindow
from Top_button_menu.layer_toggle_buttons import LayerToggleButtons
from Top_button_menu.layer_visibility_buttons import LayerVisibilityButtons
from Top_button_menu.undo_redo_buttons import UndoRedoButtons
from Drag_and_scroll_area.drag_and_scroll_area import DragScrollArea

class MainEditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tile Map Editor")

        self.setup_model = SetupModel()
        self.main_data_model = MainDataModel(self.setup_model)
        self.tile_selector = TileSelector(model=self.setup_model)
        self.tile_data_window = TileDataWindow()
        self.tile_data_window.show()
        
        self.canvas = MapCanvas(
            tile_selector=self.tile_selector,
            tile_data_view=self.tile_data_window.tile_data_view,
            model=self.main_data_model
        )
        self.main_data_model.canvas = self.canvas
        self.draw_layer_buttons = LayerToggleButtons(model=self.main_data_model)
        self.show_layer_buttons = LayerVisibilityButtons(model = self.main_data_model, canvas= self.canvas)
        self.undo_redo_buttons = UndoRedoButtons(model=self.main_data_model)

        
        # -- Canvas --
        self.canvas_scroll_area = DragScrollArea()
        self.canvas_scroll_area.setWidgetResizable(True)
        self.canvas_scroll_area.setWidget(self.canvas)
        self.canvas_scroll_area.setFixedHeight(800)
        self.canvas_scroll_area.setFixedWidth(965)

        # -- Tile selector --
        self.tile_selector_scroll = DragScrollArea()
        self.tile_selector_scroll.setWidgetResizable(True)
        self.tile_selector_scroll.setWidget(self.tile_selector)
        self.tile_selector_scroll.setFixedHeight(800)
        self.tile_selector_scroll.setFixedWidth(635)

        # -- wrapping them --
        layout = QHBoxLayout()
        layout.addWidget(self.tile_selector_scroll, stretch=1)
        layout.addWidget(self.canvas_scroll_area, stretch=1)

        content_widget = QWidget()
        content_widget.setLayout(layout)
        
        # -- Undo/Redo ---
        undo_redo_buttons = QVBoxLayout()
        undo_redo_buttons.addWidget(self.undo_redo_buttons)
        undo_redo_widget = QWidget()
        undo_redo_widget.setLayout(undo_redo_buttons)
        
        # -- Upper menu buttons --
        first_column_buttons = QVBoxLayout()
        first_column_buttons.addWidget(self.draw_layer_buttons)
        first_column_widget = QWidget()
        first_column_widget.setLayout(first_column_buttons)
        
        second_column_buttons = QVBoxLayout()
        second_column_buttons.addWidget(self.show_layer_buttons)
        second_column_widget = QWidget()
        second_column_widget.setLayout(second_column_buttons)
        
        upper_bar_layout = QHBoxLayout()
        upper_bar_layout.addWidget(first_column_widget)
        upper_bar_layout.addWidget(second_column_widget)
        upper_bar_layout.addWidget(undo_redo_widget)
        upper_bar_widget = QWidget()
        upper_bar_widget.setLayout(upper_bar_layout)
        
        # -- The final parent --
        layout_v = QVBoxLayout(self)
        layout_v.addWidget(upper_bar_widget)
        layout_v.addWidget(content_widget)
        

