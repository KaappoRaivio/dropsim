import matplotlib.pyplot as plt
import os


class Sprite:
    PIXEL_WEIGHT = 0.01
    PIXEL_WIDTH = 0.01
    def __init__(self, matrix, mass, path):
        self._matrix = matrix
        self._mass = mass

        self.path = path

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
                print(sum(pixel) / len(pixel), threshold)
                if sum(pixel) / len(pixel) > threshold:
                    mass += cls.PIXEL_WEIGHT * sum(pixel) / len(pixel)
                    matrix[y].append((0, 0, 0, 255) if not reverse else (255, 255, 255, 255))
                else:
                    # print("Moi")
                    matrix[y].append((255, 255, 255, 255) if not reverse else (0, 0, 0, 255))
        print(mass)
        return cls(matrix, mass, path)

        # print("\n".join(map("".join, matrix)))

    @property
    def area(self) -> float:
        return len(self._matrix[0]) * self.PIXEL_WIDTH

    @property
    def mass(self):
        return self._mass

    @property
    def coefficientOfDrag(self) -> float:
        return 1

    @property
    def data(self):
        return self._matrix

    @property
    def bounciness(self):
        return 0.8

    @property
    def size(self):
        return len(self._matrix[0]), len(self._matrix)


if __name__ == '__main__':
    print(Sprite.fromFile("../assets/muffincup.png"))