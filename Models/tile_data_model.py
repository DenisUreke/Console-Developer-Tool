from typing import Optional, Dict, Any

class TileData:
    def __init__(
        self,
        index: int,
        tileset: str,
        layer: str = ""
    ):
        # --- Core Visual Info ---
        self.index: int = index
        self.tileset: str = tileset
        self.layer: str = layer

        # --- Movement & Physics ---
        self.walkable: bool = True
        self.collision: Dict[str, bool] = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False
        }
        self.speed_factor: float = 1.0
        self.friction: float = 1.0
        self.bouncy: bool = False

        # --- Hazards / Environment Effects ---
        self.damage: int = 0
        self.kills_player: bool = False
        self.effect: Optional[str] = None
        self.healing: int = 0

        # --- Logic & Triggers ---
        self.trigger: Optional[str] = None
        self.target_map: Optional[str] = None
        self.target_coords: Optional[list[int]] = None
        self.event_id: Optional[str] = None
        self.script: Optional[str] = None

        # --- Spawning / Game Entities ---
        self.spawn: Optional[str] = None
        self.npc_id: Optional[str] = None
        self.item: Optional[str] = None
        self.loot_table: Optional[str] = None
        self.portal: bool = False

        # --- Structural / Type Info ---
        self.type: Optional[str] = None
        self.slope: Optional[str] = None
        self.z_index: int = 0
        self.variant: Optional[str] = None

        # --- Visual Controls ---
        self.tint: Optional[str] = None  # Hex color string
        self.alpha: float = 1.0
        self.animated: bool = False
        self.animation_id: Optional[str] = None

        # --- Metadata ---
        self.region: Optional[str] = None
        self.tag: Optional[str] = None
        self.custom_id: Optional[str] = None
        self.biome: Optional[str] = None
        self.note: Optional[str] = None

    def to_dict(self, include_fields: Optional[list[str]] = None) -> dict:
        """Convert to a dictionary, optionally filtering fields for export"""
        raw = self.__dict__.copy()
        if include_fields:
            return {k: raw[k] for k in include_fields if k in raw}
        return raw
