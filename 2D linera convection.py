#2D Linear convection
import numpy as np
from matplotlib import pyplot,cm
nx=81
ny=81
l=2
dx=2/(nx-1)
dy=2/(ny-1)
c=1
nt=100
sigma=0.1
dt=sigma*dx

x=np.linspace(0,l,nx)
y=np.linspace(0,l,ny)
u=np.ones((ny,nx))
#un=np.ones((ny,nx))
u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)]=2

for n in range(nt):
    un=u.copy()
    row,col=u.shape
    for j in range(1,row):
        for i in range(1,col):
            u[j,i]=un[j,i] - (c*dt/dx)*(un[j,i] - un[j,i-1]) - (c*dt/dy)*(un[j,i] - un[j-1,i])


            u[0, :] = 1
            u[-1, :] = 1
            u[:, 0] = 1
            u[:, -1] = 1


fig=pyplot.figure(figsize=(11,7),dpi=100)
ax=fig.gca(projection='3d')
X,Y=np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
pyplot.show()

