from math import sqrt, sin, pi
from pylab import imshow, gray, show
from numpy import empty

wavelegth = 5.0
k = 2*pi/wavelegth
xi0 = 1
sepatration = 20.0
side = 100.0
points = 500
spacing = side/points

x1 = side/2 - sepatration/2
y1 = side/2
x2 = side/2 + sepatration
y2 = side/2

pond = empty([points, points], float)

for i in range(points):

    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = sqrt((x-x1)**2 + (y-y1)**2)
        r2 = sqrt((x - x2) ** 2 + (y - y2) ** 2)
        pond[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2)


imshow(pond)
show()