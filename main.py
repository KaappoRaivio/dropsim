if __name__ != "__main__":
    raise Exception()

from scene import graphics, scene
from object import object

screen = graphics.Graphics()
scene = scene.Scene()

o = object.Object("assets/Untitled.png")  # TODO
scene.addObject(o)
scene.runForEver(screen)