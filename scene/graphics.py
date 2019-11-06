import sys, os
from typing import List

from object import object, sprite

# sys.stdout = os.devnull
import pygame
pygame.init()
# sys.stdout = sys.__stdout__


class Graphics:
    def __init__(self, size=(640,480)):
        self.size = size
        self.display = pygame.display.set_mode(size)

    def render(self, objects: List[object.Object]):
        self.display.fill((255, 255, 255, 255))

        for o in objects:
            self.fillObject(o)

        self._update()

    def fillObject(self, _object: object.Object):
        # data = _object.getSpriteData()
        #
        # for y in range(len(data)):
        #     for x in range(len(data[y])):
        #         self.display.set_at((int(_object.pos[0] + x), self.size[1] - int(_object.pos[1] + y)), data[y][x])
        image = pygame.image.load(_object.sprite.path)
        a = (int(_object.pos[0]), self.size[1] - int(_object.pos[1]) - _object.sprite.size[1])
        print(a)
        self.display.blit(image, a)

    def _update(self):
        pygame.display.flip()