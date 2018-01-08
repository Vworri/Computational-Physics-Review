from vpython import sphere, vector, color, vertex

L = 2
R = 0.3
r = 0.1


for i  in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L):
            if (j > -L and i > -L and j <= L and i <= L):
                fcc_vecor = vector(i, j, k) - vector(0.5,0.5,0)
                sphere(pos=fcc_vecor, radius=r, color=color.red)
            if (k > -L and i > -L and k <= L and i <= L):
                fcc_vecor = vector(i, j, k) - vector(0.5, 0.0, 0.5)
                sphere(pos=fcc_vecor, radius=r, color=color.cyan)
            if (k > -L and j > -L and k <= L and j <= L):
                fcc_vecor = vector(i, j, k) - vector(0.0, 0.5, 0.5)
                sphere(pos=fcc_vecor, radius=r, color=color.magenta)
            sphere(pos=vector(i, j, k), radius=R, color=color.blue)







