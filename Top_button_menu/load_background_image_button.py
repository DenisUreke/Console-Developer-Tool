from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from Models.main_data_model import MainDataModel
from PySide6.QtWidgets import QSizePolicy


class BackgroundButtons(QWidget):
    def __init__(self, model: MainDataModel):
        super().__init__()
        self.model = model
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.btn_load_1 = QPushButton("Load Background")
        self.btn_reset_1 = QPushButton("Reset Background")
        self.btn_load_2 = QPushButton("Load Background 2")
        self.btn_reset_2 = QPushButton("Reset Background 2")

        for btn in [self.btn_load_1, self.btn_reset_1, self.btn_load_2, self.btn_reset_2]:
            layout.addWidget(btn)

        self.btn_load_1.clicked.connect(lambda: self.model.load_background_image(parent=self))
        self.btn_reset_1.clicked.connect(self.reset_background_1)
        self.btn_load_2.clicked.connect(lambda: self.model.load_background_image_2(parent=self))
        self.btn_reset_2.clicked.connect(self.reset_background_2)

    def reset_background_1(self):
        self.model.background_image_layer = ""
        self.model.background_image_file_name = ""
        self.model.update_background_layer()

    def reset_background_2(self):
        self.model.background_image_layer_2 = ""
        self.model.background_image_file_name_2 = ""
        self.model.update_background_layer_2()


    
