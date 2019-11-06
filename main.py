import time

if __name__ != "__main__":
    raise Exception()

from scene import graphics, scene
from object import object

screen = graphics.Graphics()
scene = scene.Scene()

# o = object.Object("assets/muffincup.png", reverse=True)  # TODO
# o = object.Object("assets/Untitled.png", reverse=False)  # TODO
o = object.Object("assets/ball.png", reverse=True)  # TODO
# while True:
#     print(o.sprite.mass, o.sprite.area, o.pos)
#     o.updateAndMove(0.01)
#     time.sleep(0.01)
scene.addObject(o)
scene.runForEver(screen)