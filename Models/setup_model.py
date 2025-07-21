from typing import Dict

class SetupModel:
    def __init__(self):
        self.tile_size_x: int = 32
        self.tile_size_y: int = 32
        self.grid_width: int = 30
        self.grid_height: int = 20
        self.loaded_maps_index: int = 0
        self.tileset_name_dic: Dict[int, str] = {}
        
    def add_map_to_dictionary(self, name: str):
        self.tileset_name_dic[self.loaded_maps_index] = name
        self.loaded_maps_index += 1
        
