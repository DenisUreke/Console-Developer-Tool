from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Models.setup_model import SetupModel

class InitialScreen(QWidget):
    def __init__(self, model: 'SetupModel'):
        super().__init__()
        self.model = model

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)  # Just to make things more readable

        # -- Input fields (must be strings) --
        self.pixel_width = QLineEdit(str(self.model.tile_size_x))
        self.pixel_height = QLineEdit(str(self.model.tile_size_y))
        self.canvas_width = QLineEdit(str(self.model.grid_width))
        self.canvas_height = QLineEdit(str(self.model.grid_height))

        # -- Save button --
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_values)

        # -- Add to layout --
        self.layout.addWidget(QLabel("Tile Width:"))
        self.layout.addWidget(self.pixel_width)
        self.layout.addWidget(QLabel("Tile Height:"))
        self.layout.addWidget(self.pixel_height)
        self.layout.addWidget(QLabel("Grid Width:"))
        self.layout.addWidget(self.canvas_width)
        self.layout.addWidget(QLabel("Grid Height:"))
        self.layout.addWidget(self.canvas_height)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)  # Important: apply the layout to the widget

    def save_values(self):
        try:
            # Convert input values back to integers and save to model
            self.model.tile_size_x = int(self.pixel_width.text())
            self.model.tile_size_y = int(self.pixel_height.text())
            self.model.grid_width = int(self.canvas_width.text())
            self.model.grid_height = int(self.canvas_height.text())
            print("Values saved to model!")
        except ValueError:
            print("Invalid input: All fields must be integers.")
