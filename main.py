import time

if __name__ != "__main__":
    raise Exception()

from scene import graphics, scene
# from scene import scene
from object import object

screen = graphics.Graphics()
our_scene = scene.Scene(screen)

# muffincup = object.Object("assets/muffincup.png", reverse=True)  # TODO
# Untitled = object.Object("assets/Untitled.png", reverse=False)  # TODO
ball = object.Object("assets/ball.png", reverse=True, pos=(0.01, 100))  # TODO
# while True:
#     print(o.sprite.mass, o.sprite.area, o.pos)
#     o.updateAndMove(0.01)
#     time.sleep(0.01)
our_scene.addObject(ball)
our_scene.render()
input()
our_scene.runForEver()
