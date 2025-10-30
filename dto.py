from typing import TypeAlias
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def move_to(self, velocity: 'Velocity') -> 'Point':
        return Point(self.x + velocity.dx, self.y + velocity.dy)


@dataclass(frozen=True)
class Velocity:
    dx: float
    dy: float


Degree: TypeAlias = float
Radian: TypeAlias = float

Fuel: TypeAlias = int
Consumption: TypeAlias = int
