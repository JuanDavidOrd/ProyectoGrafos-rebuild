from dataclasses import dataclass
from core.models.enums import Health


@dataclass
class Donkey:
    health: Health
    age: float # los años
    energy_pct: float # de 1 a 100
    grass_kg: float
    life_ly: float # los años luz restantes


    def is_dead(self) -> bool:
        return self.life_ly <= 0 or self.energy_pct <= 0