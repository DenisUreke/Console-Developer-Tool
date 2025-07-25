# sprite_controls.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtCore import Qt
import os
import json
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Sprite_tileset_creator.sprite_data_model import SpriteDataModel
    from Sprite_tileset_creator.sprite_data_view import SpriteDataView

class SpriteControls(QWidget):
    def __init__(self, model: 'SpriteDataModel', selector, canvas, sprite_view: 'SpriteDataView', parent=None):
        super().__init__(parent)
        self.model = model
        self.selector = selector
        self.sprite_view = sprite_view
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
        
        # Export Jason
        export_button = QPushButton("Export JSON")
        export_button.clicked.connect(self.sprite_view.export_model_to_json)
        layout.addWidget(export_button)
        #

        # Load & save full project…
        b3 = QPushButton("Export Sprite Data")
        b3.clicked.connect(self._save_project)
        layout.addWidget(b3)
        #b4 = QPushButton("Load Project")
        # b4.clicked.connect(self._load_project)
        #layout.addWidget(b4)
    

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
        


    def _save_project(self):
        # 1. Ask user for project name
        project_name, ok = QInputDialog.getText(self, "Project Name", "Enter project name:")
        if not ok or not project_name.strip():
            QMessageBox.warning(self, "Cancelled", "No project name provided.")
            return

        project_name = project_name.strip()

        # 2. Ask user for folder to save the project
        folder_path = QFileDialog.getExistingDirectory(self, "Choose Folder to Save Project")
        if not folder_path:
            return  # user cancelled

        # 3. Create the project subfolder
        full_project_path = os.path.join(folder_path, project_name)
        os.makedirs(full_project_path, exist_ok=True)

        # 4. Save image
        image_path = os.path.join(full_project_path, f"{project_name}-sprite_sheet.png")
        self.canvas.export_as_image(image_path)

        # 5. Save JSON
        if hasattr(self, "sprite_view"):
            self.sprite_view.save_values_to_model()
            json_data = json.dumps(self.sprite_view.model.__dict__, indent=4)

            json_path = os.path.join(full_project_path, f"{project_name}-sprite_data.json")
            with open(json_path, "w") as f:
                f.write(json_data)

        # 6. Notify user
        QMessageBox.information(self, "Project Saved", f"Project '{project_name}' saved to:\n{full_project_path}")
        self.status.setText(f"Project saved: {full_project_path}")

