

class SpriteExportData:
    def __init__(self):
        
        # --- Type of Object ---
        self.is_single_image_rotation: bool = False
        self.is_player_character: bool = False
        self.is_npc: bool = False
        self.is_enemy: bool = False
        self.is_tile_object: bool = False
        
        # --- Tiles per Image ---
        self.moving_up: int = 0
        self.moving_up_right: int = 0
        self.moving_right: int = 0
        self.moving_down_right: int = 0
        self.moving_down: int = 0
        self.moving_down_left: int = 0
        self.moving_left: int = 0
        self.moving_up_left: int = 0
        self.attack_1: int = 0
        self.attack_2: int = 0
        self.attack_3: int = 0
        self.death: int = 0
        self.climb: int = 0
        self.idle: int = 0
        self.run: int = 0
        self.jump: int = 0
        self.push: int = 0
        self.object_animation: int = 0
        
        # --- Genera Data ---
        self.is_solid = False
        
        # --- Enemy Data ---
        self.damage_done: int = 0