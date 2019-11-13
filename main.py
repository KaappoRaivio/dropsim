import time

if __name__ != "__main__":
    raise Exception()

from scene import graphics, scene
# from scene import scene
from object import object

screen = graphics.Graphics()
our_scene = scene.Scene(screen)

ball = object.Object("assets/ball.png", reverse=True, pos=(-0.02, 50), air_resistance=False)  # TODO
ball2 = object.Object("assets/ball.png", reverse=True, pos=(0.01, 50), C=1)  # TODO

our_scene.addObjects((ball, ball2))
our_scene.render()
our_scene.runForEver()
