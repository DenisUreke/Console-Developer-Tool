from PySide6.QtWidgets import QWidget, QFormLayout, QLabel, QCheckBox, QLineEdit, QPushButton, QFileDialog
from PySide6.QtGui import QFont
from Sprite_tileset_creator.sprite_export_data import SpriteExportData
import json

class SpriteDataView(QWidget):
    def __init__(self):
        super().__init__()

        self.model = SpriteExportData()
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Editable fields dictionary: { field_name: QLineEdit }
        self.fields = {}

        # --- Type of Object ---
        self.is_single_image_rotation = QCheckBox()

        #self.layout.addRow(self.create_section_header("Type:"), QLabel())
        self.layout.addRow("Single Sprite", self.is_single_image_rotation)

        # --- Tiles per Image Section ---
        self.layout.addRow(self.create_section_header("Tile Count:"), QLabel())

        self.add_editable_field("Up", "moving_up")
        self.add_editable_field("Up-Right", "moving_up_right")
        self.add_editable_field("Right", "moving_right")
        self.add_editable_field("Down-Right", "moving_down_right")
        self.add_editable_field("Down", "moving_down")
        self.add_editable_field("Down-Left", "moving_down_left")
        self.add_editable_field("Left", "moving_left")
        self.add_editable_field("Up-Left", "moving_up_left")
        self.add_editable_field("Attack 1", "attack_1")
        self.add_editable_field("Attack 2", "attack_2")
        self.add_editable_field("Attack 3", "attack_3")
        self.add_editable_field("Death", "death")
        self.add_editable_field("Climb", "climb")
        self.add_editable_field("Idle", "idle")
        self.add_editable_field("Run", "run")
        self.add_editable_field("Jump", "jump")
        self.add_editable_field("Push", "push")
        self.add_editable_field("Object Animation", "object_animation")

        # --- Save Button ---
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_values_to_model)
        self.layout.addRow(self.save_button)

    def create_section_header(self, text: str) -> QLabel:
        label = QLabel(text)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        label.setFont(font)
        return label

    def add_editable_field(self, label: str, attr_name: str):
        line_edit = QLineEdit(str(getattr(self.model, attr_name)))
        self.layout.addRow(label, line_edit)
        self.fields[attr_name] = line_edit

    def save_values_to_model(self):
        for attr_name, line_edit in self.fields.items():
            text = line_edit.text()
            try:
                value = int(text)
            except ValueError:
                value = text
            setattr(self.model, attr_name, value)

        self.model.is_single_image_rotation = self.is_single_image_rotation.isChecked()

        print("Model updated:", vars(self.model))
        

    def export_model_to_json(self):
            # 1. Update the model with user input
            self.save_values_to_model()

            # 2. Convert model to JSON string
            json_string = json.dumps(self.model.__dict__, indent=4)

            # 3. Let the user choose where to save it
            path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Sprite Data as JSON",
                "sprite_data.json",  # default filename
                "JSON Files (*.json)"
            )

            if not path:
                return  # user canceled

            # 4. Save to file
            with open(path, "w") as f:
                f.write(json_string)

            print(f" Exported to: {path}")


