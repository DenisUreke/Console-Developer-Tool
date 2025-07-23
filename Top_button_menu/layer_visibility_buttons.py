from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QButtonGroup, QVBoxLayout, QLabel
from Models.main_data_model import MainDataModel

class LayerVisibilityButtons(QWidget):
    def __init__(self, model: MainDataModel, canvas):
        super().__init__()
        
        self.model = model
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        self.canvas = canvas
        
        title_label = QLabel("Show Layer")
        layout.addWidget(title_label)
        
        self.btn_lower = QPushButton("Lower Layer")
        self.btn_middle = QPushButton("Middle Layer")
        self.btn_upper = QPushButton("Upper Layer")
        self.btn_grid = QPushButton("Grid Layer")
        self.btn_background = QPushButton("Background Image")
        self.btn_background_2 = QPushButton("Background Image 2")
        
        for btn in [self.btn_background, self.btn_background_2, self.btn_lower, self.btn_middle, self.btn_upper, self.btn_grid]:
            btn.setCheckable(True)
            layout.addWidget(btn)
        
        self.btn_lower.setChecked(True)
        self.btn_middle.setChecked(True)
        self.btn_upper.setChecked(True)
        self.btn_grid.setChecked(True)
        self.btn_background.setChecked(True)
        self.btn_background_2.setChecked(True)
        
        self.btn_lower.clicked.connect(lambda: self.toggle_layer_visibility("lower_layer"))
        self.btn_middle.clicked.connect(lambda: self.toggle_layer_visibility("middle_layer"))
        self.btn_upper.clicked.connect(lambda: self.toggle_layer_visibility("upper_layer"))
        self.btn_grid.clicked.connect(lambda: self.toggle_layer_visibility("grid_layer"))
        self.btn_background.clicked.connect(lambda: self.toggle_layer_visibility("background_image_layer_view"))
        self.btn_background_2.clicked.connect(lambda: self.toggle_layer_visibility("background_image_layer_view_2"))
        
    def toggle_layer_visibility(self, layer: str):
        self.model.toggle_visible_layers(layer)
        self.canvas.update_layer_visibility()
        