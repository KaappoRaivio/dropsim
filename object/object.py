from typing import Tuple
from object import physics

from object.sprite import Sprite


class Object:
    def __init__(self, path_to_sprite):
        self._x = -1
        self._y = -1

        self.sprite = Sprite.fromFile(path_to_sprite)
        self.physics = physics.Physics()

    def updateAndMove(self, deltaTime: float) -> None:
        self._x, self._y = self.physics.getNewPosition()

    @property
    def pos(self) -> Tuple[int, int]:
        return self._x, self._y
        
    def getSpriteData(self):
        return self.sprite.data
        

