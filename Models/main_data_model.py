from Models.tile_data_model import TileData
from Models.setup_model import SetupModel
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog
from collections import deque
import os

class MainDataModel:
    def __init__(self, setup_data_model: SetupModel, canvas = None):
        self.setup_data_model = setup_data_model
        self.active_layer = "lower"
        self.canvas = canvas
        
        # --- background image data ---
        self.background_image_layer: str = ""
        self.background_image_file_name: str = ""
        
        self.background_image_layer_2: str = ""
        self.background_image_file_name_2: str = ""
        
        # -- visible layers --
        self.show_lower_layer = True
        self.show_middle_layer = True
        self.show_upper_layer = True
        self.show_grid_layer = True
        self.show_background_image_layer_view = True
        self.show_background_image_layer_view_2 = True
        
        self.visible_layers = {
            "lower_layer": self.show_lower_layer,
            "middle_layer": self.show_middle_layer,
            "upper_layer": self.show_upper_layer,
            "grid_layer": self.show_grid_layer,
            "background_image_layer_view": self.show_background_image_layer_view,
            "background_image_layer_view_2": self.show_background_image_layer_view_2
        }
        
        # -- undo values --
        self.undo_list: deque[TileData] = deque(maxlen=20) 
        self.undo_list_index = -1 # index for undo

        # -- tile data --
        self.tile_dictionary: dict[tuple[int, int], dict[str, TileData]] = {}

        self.grid = [[None for _ in range(self.setup_data_model.grid_width)] 
                     for _ in range(self.setup_data_model.grid_height)]

        for y in range(self.setup_data_model.grid_height):
            for x in range(self.setup_data_model.grid_width):
                self.tile_dictionary[(x, y)] = {
                    'lower': TileData(x, y, None, '', 'lower'),
                    'middle': TileData(x, y, None, '', 'middle'),
                    'upper': TileData(x, y, None, '', 'upper')
                }
                
    def set_active_layer(self, layer: str):
        self.active_layer = layer
        
    def toggle_visible_layers(self, layer: str):
        if layer in self.visible_layers:
            new_value = not self.visible_layers[layer]
            self.visible_layers[layer] = new_value

            if layer == "lower_layer":
                self.show_lower_layer = new_value
            elif layer == "middle_layer":
                self.show_middle_layer = new_value
            elif layer == "upper_layer":
                self.show_upper_layer = new_value
            elif layer == "grid_layer":
                self.show_grid_layer = new_value
            elif layer == "background_image_layer_view":
                self.show_background_image_layer_view = new_value
                if self.canvas:  # Only do this if canvas has been set
                    self.canvas.background_image_layer.setVisible(new_value)
            elif layer == "background_image_layer_view_2":
                self.show_background_image_layer_view = new_value
                if self.canvas:  # Only do this if canvas has been set
                    self.canvas.background_image_layer_2.setVisible(new_value)
    
    def add_to_deque_list(self, tile: TileData):
        while self.undo_list_index > 0:
            self.undo_list.popleft()
            self.undo_list_index -= 1

        self.undo_list.appendleft(tile)
        self.undo_list_index = 0
        print(f"deque length = {len(self.undo_list)}")
        
    def undo_actions(self):
        if self.undo_list_index + 1 <= len(self.undo_list):
            old_data = self.undo_list[self.undo_list_index]
            current_data = self.tile_dictionary[(old_data.grid_x, old_data.grid_y)][old_data.layer]
            self.tile_dictionary[(old_data.grid_x, old_data.grid_y)][old_data.layer] = old_data
            self.canvas.update()
            self.undo_list[self.undo_list_index] = current_data

            if self.undo_list_index < len(self.undo_list) - 1:
                self.undo_list_index += 1

    def redo_actions(self):
        if self.undo_list_index > 0:
            self.undo_list_index -= 1
            newer_data = self.undo_list[self.undo_list_index]
            current_data = self.tile_dictionary[(newer_data.grid_x, newer_data.grid_y)][newer_data.layer]
            self.tile_dictionary[(newer_data.grid_x, newer_data.grid_y)][newer_data.layer] = newer_data
            self.canvas.update()
            self.undo_list[self.undo_list_index] = current_data
            
    def load_background_image(self, parent=None):
        file_path, _ = QFileDialog.getOpenFileName(parent, "Load Background Image", "", "Images (*.png *.jpg)")
        if file_path:
            self.background_image_file_name = os.path.basename(file_path) 
            self.set_background_image(file_path)
            self.canvas.background_image_layer.update()
            
    def load_background_image_2(self, parent=None):
        file_path, _ = QFileDialog.getOpenFileName(parent, "Load Background Image", "", "Images (*.png *.jpg)")
        if file_path:
            self.background_image_file_name_2 = os.path.basename(file_path) 
            self.set_background_image_2(file_path)
            self.canvas.background_image_layer_2.update()
            
    def set_background_image(self, path: str):
        self.background_image_layer = QPixmap(path)
        
    def set_background_image_2(self, path: str):
        self.background_image_layer_2 = QPixmap(path)
        
    def update_background_layer(self):
        self.canvas.background_image_layer.update()
        
    def update_background_layer_2(self):
        self.canvas.background_image_layer_2.update()
    
    


        



        
        

                
       
                
        
                