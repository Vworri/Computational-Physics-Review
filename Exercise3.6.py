#Chaos and the Feigenbaum plot
from numpy import arange, log
from pylab import scatter, show, xlim, plot

r = 4.0
x = 0.8
xs =[]
ys = []
def chaos(r, x):
    n =  r*x*(1 - x)
    return n


for r in arange( 1,r,0.00002):
        xs.append(r)
        ys.append(x)
        new_x = chaos(r,x)
        x=new_x
plot(xs,ys,'.')
xlim([1,4])
show()
xs = []
ys = []
