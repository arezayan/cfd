
from cProfile import label
from distutils.file_util import write_file
from unicodedata import ucd_3_2_0
import numpy as np
from matplotlib import pyplot

l=2 #in meter

nx=41
dx=(l/(nx-1))

ny=nx
dy=(l/(ny-1))

nt=5
sigma=0.3
dt=sigma * dx

x=np.linspace(0,l,nx)
y=np.linspace(0,l,ny)


u=np.zeros((ny,nx))
v=np.zeros((ny,nx))

un=np.zeros((ny,nx))
vn=np.zeros((ny,nx))

u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)]=2  #IC
v[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)]=2  #IC

un=np.ones(nx)
print(u)

for n in range(nt):
    un=u.copy() #updateing un
    for j in range(1,ny-1):
        for i in range(1,nx-1):
            u[j,i]=un[j,i] - (un[j,i]*dt/dx) * (un[j,i] - un[j,i-1]) -(vn[j,i]*dt/dy) * (un[j,i] - un[j,i-1])
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
    
    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1    


  
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');