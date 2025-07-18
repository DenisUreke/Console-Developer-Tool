from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QButtonGroup, QVBoxLayout, QLabel
from Models.main_data_model import MainDataModel

class LayerVisibilityButtons(QWidget):
    def __init__(self, model: MainDataModel):
        super().__init__()
        
        self.model = model
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        
        title_label = QLabel("Show Layer")
        layout.addWidget(title_label)
        
        self.btn_lower = QPushButton("Lower Layer")
        self.btn_middle = QPushButton("Middle Layer")
        self.btn_upper = QPushButton("Upper Layer")
        
        for btn in [self.btn_lower, self.btn_middle, self.btn_upper]:
            btn.setCheckable(True)
            layout.addWidget(btn)
        
        self.btn_lower.setChecked(True)
        self.btn_middle.setChecked(True)
        self.btn_upper.setChecked(True)
        
        self.btn_lower.clicked.connect(lambda: self.toggle_layer_visibility("lower_layer"))
        self.btn_middle.clicked.connect(lambda: self.toggle_layer_visibility("middle_layer"))
        self.btn_upper.clicked.connect(lambda: self.toggle_layer_visibility("upper_layer"))
        
    def toggle_layer_visibility(self, layer: str):
        self.model.toggle_visible_layers(layer)
        self.parent().canvas.update_layer_visibility()
        