# sprite_controls.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtCore import Qt
import os
import json

class SpriteControlsMain(QWidget):
    def __init__(self, selector):
        super().__init__()
        self.selector = selector

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        # Load tileset
        b1 = QPushButton("Load Sprite‑Sheet")
        b1.clicked.connect(self.selector.load_tileset_dialog)
        layout.addWidget(b1)

        # Spacer + status label
        layout.addStretch()
        self.status = QLabel()
        self.status.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(self.status)

