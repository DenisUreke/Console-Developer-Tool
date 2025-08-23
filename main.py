import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from Main_editor_window.main_editor_window import MainEditorWindow
from Sprite_tileset_creator.sprite_tileset_window import SpriteTilesetWindow
from Sprite_tile_selector_window.sprite_selector_window import SpriteTilesetWindowMain
from Models.setup_model import SetupModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_model = SetupModel()
        # Use your existing QWidget as the central widget
        self.editor = MainEditorWindow(self.setup_model)
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

       # --- Tile-Set ---
        tile_set_menu = menu_bar.addMenu("Tile-Set")
        tile_set = QAction("Load new tile-set", self)
        tile_set.triggered.connect(self.load_tileset)
        tile_set_menu.addAction(tile_set)
        
       # --- Sprite-tile-Set ---
        sprite_tile_set_menu = menu_bar.addMenu("Sprite-tile-Set")
        sprite_tile_set = QAction("Create new sprite tile-set", self)
        sprite_tile_set_load = QAction("Load sprite tile-set", self)
        sprite_tile_set.triggered.connect(self.create_sprite_tileset)
        sprite_tile_set_load.triggered.connect(self.load_sprite_tilesets)
        sprite_tile_set_menu.addAction(sprite_tile_set)
        sprite_tile_set_menu.addAction(sprite_tile_set_load)
        

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
    
    def create_sprite_tileset(self):
        # keep a reference so it doesn’t get garbage-collected
        if not hasattr(self, "_sprite_tileset_window"):
            self._sprite_tileset_window = SpriteTilesetWindow(self)
        self._sprite_tileset_window.show()
        self._sprite_tileset_window.raise_()
        self._sprite_tileset_window.activateWindow()
    
    def load_sprite_tilesets(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Sprite Tilesheet",
            r"C:\Sprite-Tilesets",
            "PNG Files (*.png)"
        )

        if file_path:
            # keep a reference so it’s not garbage-collected
            if not hasattr(self, "_sprite_tileset_window_main"):
                self._sprite_tileset_window_main = SpriteTilesetWindowMain(image_path=file_path, parent=self, model=self.setup_model)
            else:
                self._sprite_tileset_window_main.close()
                self._sprite_tileset_window_main = SpriteTilesetWindowMain(image_path=file_path, parent=self, model=self.setup_model)

            self._sprite_tileset_window_main.show()
            self._sprite_tileset_window_main.raise_()
            self._sprite_tileset_window_main.activateWindow()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
