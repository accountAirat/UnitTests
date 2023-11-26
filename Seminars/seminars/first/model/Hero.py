from typing import List


class Hero:

    def __init__(self, name: str, armor_strength: str, weapon_type: str, inventory: List[str], is_human: bool):
        self.name = name
        self.armor_strength = armor_strength
        self.weapon_type = weapon_type
        self.inventory = inventory
        self.is_human = is_human

# гетеры и сетеры
