import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from Main_editor_window.main_editor_window import MainEditorWindow  # ✅ Ensure this import path is correct

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Use your existing QWidget as the central widget
        self.editor = MainEditorWindow()
        self.setCentralWidget(self.editor)

        self.setWindowTitle("Retro Tile Map Editor")
        self.resize(1600, 900)
        self.create_menus()

    def create_menus(self):
        menu_bar = self.menuBar()

        # --- File Menu ---
        file_menu = menu_bar.addMenu("File")
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close)
        open_action.triggered.connect(self.load_tileset)

        # --- Edit Menu ---
        edit_menu = menu_bar.addMenu("Edit")
        undo_action = QAction("Undo", self)
        redo_action = QAction("Redo", self)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        # --- Window Menu ---
        window_menu = menu_bar.addMenu("Window")
        window_action = QAction("Tile Data View", self)
        window_action.triggered.connect(self.show_tile_data_window)
        window_menu.addAction(window_action)


        # --- Help Menu ---
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        help_menu.addAction(about_action)

        
    def load_tileset(self):
        print("Open clicked! Load your tileset here.")
    # forward the call to the TileSelector:
        self.editor.tile_selector.load_tileset_dialog()
    
    def show_tile_data_window(self):
    # This function runs when you click the "Tile Data View" menu item
        self.editor.tile_data_window.show()
        self.editor.tile_data_window.raise_()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
