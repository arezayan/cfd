from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE
import numpy as np
from matplotlib import pyplot,cm

l,w=2,2
nx=31
ny=nx
dx=l/(nx-1)
dy=w/(ny-1)

nt=44
nu=0.05
sigma=0.25
dt=sigma * dx * dy / nu

x=np.linspace(0,l,nx)
y=np.linspace(0,w,ny)
X,Y=np.meshgrid(x,y)

u=np.zeros((ny,nx))
u[:,:]=1
u[int(0.5/dy): int(1/dy + 1),int(0.5/dx): int(1/dx + 1)] = 2

un=np.zeros((ny,nx))

for n in range(nt + 1):
    un=u.copy()
    ''' usual notation
    for i in range(nx-1):
        for j in range(ny-1):
            u[j,i]=un[j,i] + ((nu*dt/(dx**2))*(un[j,i+1] - 2 * un[j,i] + un[j,i-1])) + ((nu*dt/(dy**2))*(un[j+1,i] - 2 * un[j,i] + un[j-1,i]))'''
    u[1:-1, 1:-1] = (un[1:-1,1:-1] + 
                        nu * dt / dx**2 * 
                        (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                        nu * dt / dy**2 * 
                        (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))
    u[0,:]=1
    u[-1,:]=1
    u[:,0]=1
    u[:,-1]=1
        
        
fig=pyplot.figure(dpi=100)
ax=fig.gca(projection='3d')
surf=ax.plot_surface(X,Y,u[:],rstride=1, cstride=1, cmap=cm.viridis,linewidth=0, antialiased=False)
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_zlim(1, 2.5)
pyplot.show()
#print(u)


