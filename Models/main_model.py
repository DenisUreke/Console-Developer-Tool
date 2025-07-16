from Models.tile_data_model import TileData
from Models.setup_model import SetupModel

class mainDataModel:
    def __init__(self, setup_data_model: SetupModel ):
        self.setup_data_model = setup_data_model
        
        self.tile_dictionary: dict[tuple[int, int], TileData] = {}
        
        for y in range(self.setup_data_model.grid_height):
            for x in range(self.setup_data_model.grid_width):
                new_tile = TileData(0, '')
                self.tile_dictionary[(x, y)] = new_tile
                
        
                