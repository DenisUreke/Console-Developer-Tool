from PySide6.QtWidgets import QApplication
from tile_selector import TileSelector

app = QApplication([])
window = TileSelector(tile_size=100)  # Adjust tile_size for 32, 64, etc.
window.resize(800, 600)
window.show()
app.exec()
