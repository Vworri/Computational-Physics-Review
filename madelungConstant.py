import scipy.constants as s_const
from math import pi
#In condensed matter physics, the Madelung constant gives the total electric potential felt by an atom in a solid.
#In this program, we will use the sodium chloride wich is arranged in a cubic lattice. The vertexes of the cube alternate
#positive to negative with the same charge e. If we give each vertex three coordinates, then the sodium atoms will fall
# where j+k+i is even. The chloride atoms will fall where i+j+k is odd.

#We also know that the Madelung constant is equal to the summation of of the potential energy of all the atoms in the
#lattice divided by  (4*pi*epsilon_0)*the spacing of the lattice.
#The potential enery of a charge is Q/4*pi*epsilon*r with r being the distance between the atom and the origin.
#The summation domain is from one end of the cube to the other excluding the origin.
e = s_const.elementary_charge #absolute value of electron charge
epsilon_0 = s_const.epsilon_0 # permittivity of vacuum
L = 600 #1/2 the width of the cube
a =1 #spacing of the atoms
V_tot = 0 #initial potential energy
# This works but the O^3 iteration is a bummer. I think if I let it sit at L= 1000 my computer will die
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if (i == 0 or j==0 or k==0):
                V_tot +=0
            elif ((i+j+k)%2 == 0):
                V_tot += e/(4*pi*epsilon_0*a*((i**2)+(j**2)+(k**2))**0.5)
            else:
                V_tot -= e/(4 * pi * epsilon_0 * a * ((i ** 2) + (j ** 2) + (k ** 2))**0.5)
print((V_tot*(4 * pi * epsilon_0 * a ))/e)

