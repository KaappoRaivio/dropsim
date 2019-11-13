import time
from typing import Tuple
from object import physics

from object import sprite


class Object:
    def __init__(self, path_to_sprite, reverse=False, pos=(0, 5), C=1, air_resistance=True):
        self.sprite: sprite.Sprite = sprite.Sprite.fromFile(path_to_sprite, reverse=reverse)
        self.physics = physics.Physics(A=self.sprite.area, m=self.sprite.mass, C=C, bounciness=self.sprite.bounciness, pos=pos, air_resistance=air_resistance)
        self.highest_point = pos
        self._has_started = False

    def updateAndMove(self, deltaTime: float) -> None:
        if not self._has_started:
            self._start_time = time.time()
            self._has_started = True
        self.physics.updatePosition(deltaTime)



    @property
    def pos(self) -> Tuple[int, int]:
        return self.physics.pos

    def getTimeElapsed(self):
        if self.physics.isOnGround():
            return self.physics.time_touched - self._start_time
        elif not self._has_started:
            return 0
        else:
            return time.time() - self._start_time
        
    def getSpriteData(self):
        return self.sprite.data

    def __str__(self):
        return f"a: {self.physics.a:6.2f}, v: {self.physics.v:6.2f}, pos: ({self.pos[0]:.2f}, {self.pos[1]:6.2f}), drag: {self.physics.getDrag():6.2f}, weight {self.physics.getGravitationalForce():6.2f}"
        

