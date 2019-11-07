from typing import Tuple
from object import physics

from object import sprite


class Object:
    def __init__(self, path_to_sprite, reverse=False, pos=(0, 5)):
        self.sprite: sprite.Sprite = sprite.Sprite.fromFile(path_to_sprite, reverse=reverse)
        self.physics = physics.Physics(A=self.sprite.area, m=self.sprite.mass, C=self.sprite.coefficientOfDrag, bounciness=self.sprite.bounciness, pos=pos)

    def updateAndMove(self, deltaTime: float) -> None:
        self.physics.updatePosition(deltaTime)

    @property
    def pos(self) -> Tuple[int, int]:
        return self.physics.pos
        
    def getSpriteData(self):
        return self.sprite.data

    def __str__(self):
        return f"a: {self.physics.a:6.2f}, v: {self.physics.v:6.2f}, pos: ({self.pos[0]:.2f}, {self.pos[1]:6.2f}), drag: {self.physics.getDrag():6.2f}, weight {self.physics.getGravitationalForce():6.2f}"
        

