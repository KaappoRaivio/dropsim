from typing import Tuple
from object import physics

from object import sprite


class Object:
    def __init__(self, path_to_sprite):
        self._x = -1
        self._y = -1

        self.sprite: sprite.Sprite = sprite.Sprite.fromFile(path_to_sprite)
        self.physics = physics.Physics(A=self.sprite.area, m=self.sprite.mass, C=self.sprite.coefficientOfDrag)

    def updateAndMove(self, deltaTime: float) -> None:
        self._x, self._y = self.physics.updatePosition()

    @property
    def pos(self) -> Tuple[int, int]:
        return self._x, self._y
        
    def getSpriteData(self):
        return self.sprite.data

    def __str__(self):
        return f"a: {self.physics.a}, v: {self.physics.v}, pos: {self.pos}"
        

