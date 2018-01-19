from vpython import sphere, rate, vector, color
from scipy.constants import day
from math import pi, cos ,sin
from numpy import arange

ScalingFactor = 0.0025

class planetInfo():
    def __init__(self,Radius, Orbit, Period, c):

        SunRadius = 6955500.0*ScalingFactor
        self.radius = Radius
        self.orbit = Orbit
        self.period = Period
        self.planet = sphere(pos=vector((self.orbit + SunRadius), self.orbit ,0), radius=self.radius*ScalingFactor,color = c)
        return

    def updatepos(self, x, y):
        self.planet.pos = vector(x,y,0)
        return self.planet



Mercury = planetInfo(2440.0, 57.9,88.0, color.orange)

Venus = planetInfo(6052.0,108.2, 224.7, color.blue)

Earth = planetInfo(6371.0,149.6,  365.3, color.green)

Mars = planetInfo( 3386.0, 227.9,  687.0,color.red)

Jupyter = planetInfo(69173.0,778.5, 4331.6, color.cyan)

Saturn = planetInfo(57316.0, 1433.4, 10759.2, color.magenta)


SunRadius = 6955500.0
sphere(pos=vector(0,0,0), radius= SunRadius*ScalingFactor, color = color.yellow)

planets = [Mercury, Venus,Earth,Mars, Jupyter, Saturn]



#
# for theta in arange(0, 10*pi, 0.1):
#     rate(30)
#     for planet in planets:
#         x = cos(theta)
#         y =sin(theta)
#         planet.updatepos(x,y)
