from Models.tile_data_model import TileData
from Models.setup_model import SetupModel
from collections import deque

class MainDataModel:
    def __init__(self, setup_data_model: SetupModel):
        self.setup_data_model = setup_data_model
        self.active_layer = "lower"
        
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
        self.undo_list: deque[TileData] = deque(maxlen=10) 
        self.undo_list_index = len(self.undo_list) -1 # index for undo

        # -- tile data --
        self.tile_dictionary: dict[tuple[int, int], dict[str, TileData]] = {}

        self.grid = [[None for _ in range(self.setup_data_model.grid_width)] 
                     for _ in range(self.setup_data_model.grid_height)]

        for y in range(self.setup_data_model.grid_height):
            for x in range(self.setup_data_model.grid_width):
                self.tile_dictionary[(x, y)] = {
                    'lower': TileData(0, '', 'lower'),
                    'middle': TileData(0, '', 'middle'),
                    'upper': TileData(0, '', 'upper')
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
        self.undo_list.appendleft(tile)
        
    def undo_actions(self):
        if self.undo_list_index > -1:
            old_data = self.undo_list[self.undo_list_index]
            pass
        


        
        

                
       
                
        
                