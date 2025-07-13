import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from PySide6.QtCore import Qt
from Tile_editor.tile_editor import MainEditorWindow  # ✅ This is your main window with both canvas & selector

def main():
    app = QApplication(sys.argv)

    window = MainEditorWindow()
    window.resize(1600, 900)
    window.setWindowTitle("Retro Tile Map Editor")
    window.setWindowFlag(Qt.Window)
    window.show()

    sys.exit(app.exec())
    
def create_menus(self):
        # Get the menu bar (automatically placed at the top)
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

        exit_action.triggered.connect(self.close)  # Close app when Exit is clicked

        # --- Edit Menu ---
        edit_menu = menu_bar.addMenu("Edit")
        undo_action = QAction("Undo", self)
        redo_action = QAction("Redo", self)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        # --- Help Menu ---
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        help_menu.addAction(about_action)


if __name__ == "__main__":
    app = QApplication([])
    window = MainEditorWindow()
    window.show()
    app.exec()
