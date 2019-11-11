import sys, os
from typing import List

from object import object, sprite
from scene import scene

# sys.stdout = os.devnull
import pygame
pygame.init()
# sys.stdout = sys.__stdout__


class Graphics:
    def __init__(self, size=(640,480)):
        self.size = size
        self.display = pygame.display.set_mode(size)

        self._scene = scene

    def render(self, _scene: scene.Scene, objects: List[object.Object]):
        self.display.fill((255, 255, 255, 255))

        for o in objects:
            self.fillObject(_scene, o)

        self._update()

    def fillObject(self, _scene: scene.Scene, _object: object.Object):
        image = pygame.image.load(_object.sprite.path)

        highest_point = _scene.getHighestPoint()[1]
        position_in_meters = _object.pos
        pixel_dimen = sprite.Sprite.PIXEL_DIMEN
        # position_in_pixels = tuple(map(lambda x: x / pixel_dimen, position_in_meters))

        position_in_pixels = self.size[0]/2 + position_in_meters[0] / pixel_dimen - _object.sprite.size[0]/2, self.size[1] - self.size[1] * position_in_meters[1] / highest_point - _object.sprite.size[1]
        print(position_in_pixels)

        self.display.blit(image, position_in_pixels)

    def _update(self):
        pygame.display.flip()
