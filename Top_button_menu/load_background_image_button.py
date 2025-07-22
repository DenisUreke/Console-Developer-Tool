from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QButtonGroup, QVBoxLayout, QLabel
from Models.main_data_model import MainDataModel

class LoadBackgroundImageButton(QWidget):
    def __init__(self, model: MainDataModel):
        super().__init__()
        self.model = model

        layout = QVBoxLayout(self)
        btn_load_background = QPushButton("Load Background")
        btn_load_background.clicked.connect(self.load_background_image)
        layout.addWidget(btn_load_background)
        
    def load_background_image(self):
        self.model.load_background_image(parent=self) 
    
