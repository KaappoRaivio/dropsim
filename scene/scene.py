import time
from typing import List

from object import object
from scene import graphics

class Scene:
    def __init__(self):
        self._objects: List[object.Object] = []
        self.previous_times = []

    def addObject(self, object: object.Object):
        self._objects.append(object)
        self.previous_times.append(time.time())


    def addObjects(self, objects: List[object.Object]):
        if objects:
            self.addObject(objects[1])
            self.addObjects(objects[1:])

    def update(self):
        for index, o in enumerate(self._objects):
            time = self._getDeltaTime(index)
            o.updateAndMove(time)

    def _getDeltaTime(self, index: int):
        previous = self.previous_times[index]
        self.previous_times[index] = time.time()
        return (self.previous_times[index] - previous) * 3

    def runForEver(self, screen: graphics.Graphics):
        while KeyboardInterrupt:
            self.update()
            screen.render(self._objects)
            time.sleep(0.1)
            print(self._objects[0])