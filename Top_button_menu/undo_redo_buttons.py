from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel
from Models.main_data_model import MainDataModel

class UndoRedoButtons(QWidget):
    def __init__(self, model: MainDataModel):
        super().__init__()
        self.model = model
        
        layout = QHBoxLayout(self)
        
        title_label = QLabel("Undo / Redo")
        
        self.btn_undo = QPushButton("Undo")
        self.btn_redo = QPushButton("Redo")
        
        self.btn_undo.clicked.connect(lambda: self.undo_redo("undo"))
        self.btn_redo.clicked.connect(lambda: self.undo_redo("redo"))
        
        layout.addWidget(self.btn_undo)
        layout.addWidget(self.btn_redo)
        
    def undo_redo(self, operation: str):
        if operation == "undo":
            self.model.undo_actions()
        else:
            self.model.redo_actions()
        
        
        
        
        
        
        
        
        