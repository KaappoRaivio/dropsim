from typing import Tuple
import physics


class Object:
    def __init__(self, path_to_sprite):
        self._x = -1, self._y = -1

    def updateAndMove(self, deltaTime: float) -> None:
        self._x, self._y = physics.getNewPosition()

    @property
    def pos(self) -> Tuple[int, int]:
	return self._x, self._y
