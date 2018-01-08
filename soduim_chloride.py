from vpython import sphere, vector, color
L = 5
R = 0.3
r = 0.1
sodium = True
for i  in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if (sodium == True):
                sphere(pos=vector(i, j, k), radius=R, color=color.blue)
                sodium = False
            elif (sodium == False):
                sphere(pos=vector(i,j,k), radius = r, color= color.red)
                sodium = True