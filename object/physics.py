from typing import Tuple

class Physics:
    def __init__(self):
        pass

    def calculateNewPosition(self, pos, v, dt) -> Tuple[float, float]:
        # pos   : previous position
        # v     : velocity
        # dt    : delta time

        return pos[0], pos[1] - v/dt

    def calculateGravitationalForce(self, g, m) -> float:
        # g     : gravitational acceleration
        # m     : mass

        return g * m

    def calculateNewDragForce(self, rho, C, A, v) -> float:
        # rho   : density of air
        # C     : coefficient of drag
        # A     : area of object's face
        # v     : velocity

        return rho * C * A * (v ** 2)

    def calculateNewAcceleration(self, G, F, m) -> float:
        # G     : gravitational force
        # F     : drag force
        # m     : mass

        return (G - F) / m

    def calculateNewVelocity(self, v, a) -> float:
        # v     : previous velocity
        # a     : acceleration

        return v + a
