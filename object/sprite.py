import matplotlib.pyplot as plt
import os


class Sprite:
    def __init__(self, matrix):
        self._matrix = matrix

    def normalizeData(self):
        return

    @classmethod
    def fromFile(cls, path, threshold=0.5):
        data = plt.imread(path)
        # print(data)

        matrix = []

        for y, row in enumerate(data):
            matrix.append([])
            for x, pixel in enumerate(row):
                if sum(pixel) / len(pixel) > threshold:
                    matrix[y].append("1")
                else:
                    matrix[y].append("0")

        # print("\n".join(map("".join, matrix)))

    def getArea(self) -> float:
        return 1

    def getCoefficientOfDrag(self) -> float:
        return 1

    @property
    def data(self):
        return self._matrix

if __name__ == '__main__':
    print(Sprite.fromFile("../assets/Untitled.png"))