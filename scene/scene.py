from typing import List

from object import object

class Scene:
    def __init__(self):
        self._objects: List[object.Object] = []

    def addObject(self, object: object.Object):
        self._objects.append(object)

    def update(self):
        for o in self._objects:
            o.getNewPos()



