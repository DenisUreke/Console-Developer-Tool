from Models.tile_data_model import TileData
from Models.setup_model import SetupModel

class mainDataModel:
    def __init__(self, setup_data_model: SetupModel):
        self.setup_data_model = setup_data_model
        self.active_layer = "lower"

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

                
       
                
        
                