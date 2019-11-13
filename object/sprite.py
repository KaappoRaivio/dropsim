import math
import matplotlib.pyplot as plt
import os

import pygame


class Sprite:
    PIXEL_WEIGHT = 0.01
    PIXEL_DIMEN = 0.195 / 1080

    def __init__(self, matrix, mass, path):
        self._matrix = matrix
        self._mass = mass

        self._path = path

        self._sufrace = pygame.image.load(self._path)
        self._original_size = self._sufrace.get_rect().size

    def normalizeData(self):
        return

    @classmethod
    def fromFile(cls, path, threshold: float=0.5, reverse: bool=False):
        data = plt.imread(path)
        # print(data)

        matrix = []
        mass = 0

        for y, row in enumerate(reversed(data)):
            matrix.append([])
            for x, pixel in enumerate(row):
                if sum(pixel) / len(pixel) > threshold:
                    mass += cls.PIXEL_WEIGHT * sum(pixel) / len(pixel)
                    matrix[y].append((0, 0, 0, 255) if not reverse else (255, 255, 255, 255))
                else:
                    matrix[y].append((255, 255, 255, 255) if not reverse else (0, 0, 0, 255))

        return cls(matrix, mass, path)

        # print("\n".join(map("".join, matrix)))

    @property
    def area(self) -> float:
        return len(self._matrix[0]) * math.sqrt(self.PIXEL_DIMEN)

    @property
    def mass(self):
        return self._mass

    @property
    def coefficientOfDrag(self) -> float:
        return 0.4

    @property
    def data(self):
        return self._matrix

    @property
    def bounciness(self):
        return 0.8

    @property
    def size(self):
        # return len(self._matrix[0]), len(self._matrix)
        return self._sufrace.get_rect().size

    @property
    def original_size(self):
        return self._original_size

    def rescale(self, size):
        self._sufrace = pygame.transform.scale(self._sufrace, size)

    def getImageSurface(self):
        return self._sufrace


if __name__ == '__main__':
    print(Sprite.fromFile("../assets/muffincup.png"))