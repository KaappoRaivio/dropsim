from typing import List

from object import object

class Scene:
    def __init__(self):
        self._objects: List[object.Object] = []

    def addObject(self, object: object.Object):
        self._objects.append(object)

    def update(self):
        for index, o in enumerate(self._objects):
            o.updateAndMove(self._getDeltaTime(index))

    def _getDeltaTime(self, index: int):
        return 0.01




