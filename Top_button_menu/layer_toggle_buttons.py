from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QButtonGroup, QVBoxLayout, QLabel
from Models.main_data_model import MainDataModel

class LayerToggleButtons(QWidget):
    def __init__(self, model: MainDataModel):
        super().__init__()
        
        self.model = model
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        
        title_label = QLabel("Draw Layer")
        layout.addWidget(title_label)

        # Create toggle buttons
        self.btn_lower = QPushButton("Lower Layer")
        self.btn_middle = QPushButton("Middle Layer")
        self.btn_upper = QPushButton("Upper Layer")
        

        for btn in [self.btn_lower, self.btn_middle, self.btn_upper]:
            btn.setCheckable(True)
            layout.addWidget(btn)

        # Group the buttons to allow only one checked at a time
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)
        self.button_group.addButton(self.btn_lower)
        self.button_group.addButton(self.btn_middle)
        self.button_group.addButton(self.btn_upper)

        # Set default active layer
        self.btn_lower.setChecked(True)
        self.model.active_layer = "lower"

        # Connect signals
        self.btn_lower.clicked.connect(lambda: self.set_active_layer("lower"))
        self.btn_middle.clicked.connect(lambda: self.set_active_layer("middle"))
        self.btn_upper.clicked.connect(lambda: self.set_active_layer("upper"))

    def set_active_layer(self, layer: str):
        self.model.set_active_layer(layer=layer)
