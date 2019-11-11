from typing import Tuple

class Physics:
    def __init__(self, pos=(0, 100), v=0, a=0, m=1, g=10, rho=1.23, C=1, A=1, bounciness=0.5):
        # pos   : position of the object
        # v     : velocity of the object
        # a     : acceleration of the object
        # dt    : delta time i. e. amount of time passed
        # m     : mass of the objegetNewct
        # g     : gravitational acceleration
        # rho   : density of air
        # C     : drag coefficient of the object
        # A     : face area of the object

        self.bounciness = bounciness
        self.pos = pos

        self.v = v
        
        self.a = a

        self.m = m

        self.g = g

        self.rho = rho

        self.C = C

        self.A = A

    def updatePosition(self, dt) -> Tuple[int, int]:
        x = self.pos[0]
        y = self.pos[1]

        if y <= 0:
            self.v = -self.v * self.bounciness
            # self.
            self.pos = self.pos[0], 0,
            return self.pos

        v = self._updateVelocity(dt)

        self.pos = (x, y - v*dt)

        return self.pos

    def _updateVelocity(self, dt) -> float:
        v = self.v
        a = self._updateAcceleration()

        self.v = v + a*dt

        return self.v

    def _updateAcceleration(self) -> float:
        G = self.getGravitationalForce()
        F = self.getDrag()
        m = self.m

        self.a = (G - abs(F)) / m

        return self.a

    def getGravitationalForce(self) -> float:
        g = self.g
        m = self.m

        return g * m

    def getDrag(self) -> float:
        rho = self.rho
        C = self.C
        A = self.A
        v = self.v

        return 0.5 * rho * C * A * (v ** 2)

