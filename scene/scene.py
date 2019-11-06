import time
from typing import List

from object import object
from scene import graphics

class Scene:
    def __init__(self):
        self._objects: List[object.Object] = []

    def addObject(self, object: object.Object):
        self._objects.append(object)

    def addObjects(self, objects: List[object.Object]):
        if objects:
            self.addObject(objects[1])
            self.addObjects(objects[1:])

    def update(self):
        for index, o in enumerate(self._objects):
            print(o.pos)
            o.updateAndMove(self._getDeltaTime(index))

    def _getDeltaTime(self, index: int):
        return 0.01

    def runForEver(self, screen: graphics.Graphics):
        while KeyboardInterrupt:
            self.update()
            screen.render(self._objects)
            time.sleep(0.1)