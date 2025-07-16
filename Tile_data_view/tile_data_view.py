from PySide6.QtWidgets import QWidget, QFormLayout, QLabel, QCheckBox
from Models.tile_data_model import TileData

class TileDataView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Keep references to widgets you want to update
        self.index_label = QLabel()
        self.tileset_label = QLabel()
        self.layer_label = QLabel()
        self.walkable_cb = QCheckBox()
        self.walkable_cb.setEnabled(False)

        # Collision checkboxes
        self.collision_cbs = {
            side: QCheckBox() for side in ["top", "bottom", "left", "right"]
        }
        for cb in self.collision_cbs.values():
            cb.setEnabled(False)
        
        self.speed_factor = QLabel()
        self.friction = QLabel()
        self.bouncy_cb = QCheckBox()
        self.bouncy_cb.setEnabled(False)
        
        # --- Hazards / Environment Effects ---
        self.damage = QLabel()
        self.kills_player_cb = QCheckBox()
        self.kills_player_cb.setEnabled(False)
        self.effect = QLabel()
        self.healing = QLabel()
        
        # --- Logic & Triggers ---
        self.trigger = QLabel()
        self.target_map = QLabel()
        self.target_coords = QLabel()
        self.event_id = QLabel()
        self.script = QLabel()

        # --- Spawning / Game Entities ---
        self.spawn = QLabel()
        self.npc_id = QLabel()
        self.item = QLabel()
        self.loot_table = QLabel()
        self.portal_cb = QCheckBox()
        self.portal_cb.setEnabled(False)

        # --- Structural / Type Info ---
        self.type = QLabel()
        self.slope = QLabel()
        self.z_index = QLabel()
        self.variant = QLabel()

        # --- Visual Controls ---
        self.tint = QLabel()
        self.alpha = QLabel()
        self.animated_cb = QCheckBox()
        self.animated_cb.setEnabled(False)
        self.animation_id = QLabel()

        # --- Metadata ---
        self.region = QLabel()
        self.tag = QLabel()
        self.custom_id = QLabel()
        self.biome = QLabel()
        self.note = QLabel() 
        
        # Add fields to layout
        self.layout.addRow("Index:", self.index_label)
        self.layout.addRow("Tileset:", self.tileset_label)
        self.layout.addRow("Layer:", self.layer_label)
        self.layout.addRow("Walkable:", self.walkable_cb)
        
        # --- Movement & Physics ---
        self.layout.addRow("Speed Factor:", self.speed_factor)
        self.layout.addRow("Friction:", self.friction)
        self.layout.addRow("Bouncy:", self.bouncy_cb)

        # --- Hazards / Environment Effects ---
        self.layout.addRow("Damage:", self.damage)
        self.layout.addRow("Kills Player:", self.kills_player_cb)
        self.layout.addRow("Effect:", self.effect)
        self.layout.addRow("Healing:", self.healing)

        # --- Logic & Triggers ---
        self.layout.addRow("Trigger:", self.trigger)
        self.layout.addRow("Target Map:", self.target_map)
        self.layout.addRow("Target Coords:", self.target_coords)
        self.layout.addRow("Event ID:", self.event_id)
        self.layout.addRow("Script:", self.script)

        # --- Spawning / Game Entities ---
        self.layout.addRow("Spawn:", self.spawn)
        self.layout.addRow("NPC ID:", self.npc_id)
        self.layout.addRow("Item:", self.item)
        self.layout.addRow("Loot Table:", self.loot_table)
        self.layout.addRow("Portal:", self.portal_cb)

        # --- Structural / Type Info ---
        self.layout.addRow("Type:", self.type)
        self.layout.addRow("Slope:", self.slope)
        self.layout.addRow("Z-Index:", self.z_index)
        self.layout.addRow("Variant:", self.variant)

        # --- Visual Controls ---
        self.layout.addRow("Tint:", self.tint)
        self.layout.addRow("Alpha:", self.alpha)
        self.layout.addRow("Animated:", self.animated_cb)
        self.layout.addRow("Animation ID:", self.animation_id)

        # --- Metadata ---
        self.layout.addRow("Region:", self.region)
        self.layout.addRow("Tag:", self.tag)
        self.layout.addRow("Custom ID:", self.custom_id)
        self.layout.addRow("Biome:", self.biome)
        self.layout.addRow("Note:", self.note)

        for side, cb in self.collision_cbs.items():
            self.layout.addRow(f"Collision {side}:", cb)

    def load_tile_data(self, tile_data: TileData):
        """Populate the view with new tile data"""
        self.index_label.setText(str(tile_data.index))
        self.tileset_label.setText(tile_data.tileset)
        self.layer_label.setText(tile_data.layer)
        self.walkable_cb.setChecked(tile_data.walkable)

        # Movement & Physics
        self.speed_factor.setText(str(tile_data.speed_factor))
        self.friction.setText(str(tile_data.friction))
        self.bouncy_cb.setChecked(tile_data.bouncy)

        # Hazards / Environment Effects
        self.damage.setText(str(tile_data.damage))
        self.kills_player_cb.setChecked(tile_data.kills_player)
        self.effect.setText(tile_data.effect or "")
        self.healing.setText(str(tile_data.healing))

        # Logic & Triggers
        self.trigger.setText(tile_data.trigger or "")
        self.target_map.setText(tile_data.target_map or "")
        self.target_coords.setText(str(tile_data.target_coords) if tile_data.target_coords else "")
        self.event_id.setText(tile_data.event_id or "")
        self.script.setText(tile_data.script or "")

        # Spawning / Game Entities
        self.spawn.setText(tile_data.spawn or "")
        self.npc_id.setText(tile_data.npc_id or "")
        self.item.setText(tile_data.item or "")
        self.loot_table.setText(tile_data.loot_table or "")
        self.portal_cb.setChecked(tile_data.portal)

        # Structural / Type Info
        self.type.setText(tile_data.type or "")
        self.slope.setText(tile_data.slope or "")
        self.z_index.setText(str(tile_data.z_index))
        self.variant.setText(tile_data.variant or "")

        # Visual Controls
        self.tint.setText(tile_data.tint or "")
        self.alpha.setText(str(tile_data.alpha))
        self.animated_cb.setChecked(tile_data.animated)
        self.animation_id.setText(tile_data.animation_id or "")

        # Metadata
        self.region.setText(tile_data.region or "")
        self.tag.setText(tile_data.tag or "")
        self.custom_id.setText(tile_data.custom_id or "")
        self.biome.setText(tile_data.biome or "")
        self.note.setText(tile_data.note or "")

        # Collision
        for side in self.collision_cbs:
            self.collision_cbs[side].setChecked(tile_data.collision[side])

