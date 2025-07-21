from Models.tile_data_model import TileData
from Models.setup_model import SetupModel
from collections import deque

class MainDataModel:
    def __init__(self, setup_data_model: SetupModel, canvas = None):
        self.setup_data_model = setup_data_model
        self.active_layer = "lower"
        self.canvas = canvas
        
        # -- visible layers --
        self.show_lower_layer = True
        self.show_middle_layer = True
        self.show_upper_layer = True
        self.show_grid_layer = True
        
        self.visible_layers = {
            "lower_layer": self.show_lower_layer,
            "middle_layer": self.show_middle_layer,
            "upper_layer": self.show_upper_layer,
            "grid_layer": self.show_grid_layer
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
                self.show_upper_layer = new_value
    
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


        



        
        

                
       
                
        
                