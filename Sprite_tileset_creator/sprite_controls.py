# sprite_controls.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PySide6.QtCore import Qt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Sprite_tileset_creator.sprite_data_model import SpriteDataModel

class SpriteControls(QWidget):
    def __init__(self, model: 'SpriteDataModel', selector, canvas, parent=None):
        super().__init__(parent)
        self.model = model
        self.selector = selector
        self.canvas = canvas

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        # Load tileset
        b1 = QPushButton("Load Sprite‑Sheet")
        b1.clicked.connect(self.selector.load_tileset_dialog)
        layout.addWidget(b1)

        # Save canvas as image
        b2 = QPushButton("Export Image")
        b2.clicked.connect(self._export_image)
        layout.addWidget(b2)

        # Load & save full project…
        b3 = QPushButton("Save Project")
        # b3.clicked.connect(self._save_project)
        layout.addWidget(b3)
        b4 = QPushButton("Load Project")
        # b4.clicked.connect(self._load_project)
        layout.addWidget(b4)

        # Spacer + status label
        layout.addStretch()
        self.status = QLabel()
        self.status.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(self.status)

    def _export_image(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export As…", "", "PNG files (*.png)")
        if not path:
            return
        self.canvas.export_as_image(path)
        self.status.setText(f"Exported to {path}")
