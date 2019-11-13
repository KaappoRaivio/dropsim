import sys, os
from typing import List

from object import object, sprite
from scene import scene

# sys.stdout = os.devnull
import time
import pygame
pygame.init()
# sys.stdout = sys.__stdout__


class Graphics:
    def __init__(self, size=(640,480)):
        self.size = size
        self.display = pygame.display.set_mode(size)

        self._scene = scene
        self._font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self, _scene: scene.Scene, objects: List[object.Object]):
        self.display.fill((255, 255, 255, 255))

        for o in objects:
            self.fillObject(_scene, o)

        self._update()

    def fillObject(self, _scene: scene.Scene, _object: object.Object):
        position_in_meters = _object.pos
        pixel_dimen = sprite.Sprite.PIXEL_DIMEN
        highest_point = _scene.getHighestPoint()

        scale_factor = (self.size[1] * highest_point) / (self.size[1] - _object.sprite.original_size[1])

        _object.sprite.rescale((int(_object.sprite.original_size[0] / scale_factor), int(_object.sprite.original_size[1] / scale_factor)))
        image = _object.sprite.getImageSurface()

        position_in_pixels = self.size[0]/2 + position_in_meters[0] / pixel_dimen - _object.sprite.size[0]/2, \
                             self.size[1] - self.size[1] * position_in_meters[1] / scale_factor - _object.sprite.size[1]

        text1 = self._font.render(f"t: {_object.getTimeElapsed():.2f}", False, (0, 0, 0))
        text2 = self._font.render(f"h: {_object.pos[1]:.2f}", False, (0, 0, 0))
        text3 = self._font.render(f"a: {_object.physics.a:.2f}", False, (0, 0, 0))

        self.display.blit(image, position_in_pixels)
        self.display.blit(text1, (position_in_pixels[0] + _object.sprite.size[0], position_in_pixels[1] - 50))
        self.display.blit(text2, (position_in_pixels[0] + _object.sprite.size[0], position_in_pixels[1] - 25))
        self.display.blit(text3, (position_in_pixels[0] + _object.sprite.size[0], position_in_pixels[1] - 0))

    def _update(self):
        pygame.display.flip()
