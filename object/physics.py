from typing import Tuple

class Physics:
    def __init__(self, pos=(-1, -1), v=0, a=0, dt=0.01, m=1, g=10, rho=1.23, C=1, A=1):
        # pos   : position of the object
        # v     : velocity of the object
        # a     : acceleration of the object
        # dt    : delta time i. e. amount of time passed
        # m     : mass of the object
        # g     : gravitational acceleration
        # rho   : density of air
        # C     : drag coefficient of the object
        # A     : face area of the object

        self.pos = pos

        self.v = v
        
        self.a = a

        self.dt = dt

        self.m = m

        self.g = g

        self.rho = rho

        self.C = C

        self.A = A

    def getNewPosition(self) -> Tuple[int, int]:
        x = self.pos[0]
        y = self.pos[1]
        
        v = self.getNewVelocity()
        dt = self.dt

        self.pos = (x, y - v/dt)

        return self.pos

    def getNewVelocity(self) -> float:
        v = self.v
        a = self.getNewAcceleration()
        dt = self.dt

        return v + a/dt

    def getNewAcceleration(self) -> float:
        G = self.getGravitationalForce()
        F = self.getNewDrag()
        m = self.m

        return (G - F) / m

    def getGravitationalForce(self) -> float:
        g = self.g
        m = self.m

        return g * m

    def getNewDrag(self) -> float:
        rho = self.rho
        C = self.C
        A = self.A
        v = self.v

        return 0.5 * rho * C * A * (v ** 2)

