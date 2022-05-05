#2D convection equation by FDM
import numpy as np
from matplotlib import pyplot,cm

#pre-processing
l=2 #in meter
h=2
nx=101
dx=l/(nx-1)
ny=nx
dy=h/(ny-1)

nt=101
sigma=0.2
dt=dx*sigma

#solving in 2D
u=np.zeros((ny,nx))
v=np.zeros((ny,nx))
u[:,:]=1
v[:,:]=1
u[int(0.5/dy):int((1/dy)+1),int(0.5/dx):int((1/dx)+1)]=2
v[int(0.5/dy):int((1/dy)+1),int(0.5/dx):int((1/dx)+1)]=2

print(u)

un=np.zeros((ny,nx))
vn=np.zeros((ny,nx))

for n in range(nt):
    un=u.copy()
    vn=v.copy()
    for i in range(1,nx):
        for j in range(1,ny):
            u[j, i] = un[j, i] - (un[j, i]* 1 * dt / dx * (un[j, i] - un[j,i-1])) - vn[j, i]* 1 * dt / dy * (un[j,i] - un[j-1,i])
            v[j, i] = vn[j, i] - (un[j, i]* 1 * dt / dx * (vn[j, i] - vn[j,i-1])) - vn[j, i]* 1 * dt / dy * (vn[j,i] - vn[j-1,i])
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
    
    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1

#post-processing
x=np.linspace(0,l,nx)
y=np.linspace(0,h,ny)
X,Y=np.meshgrid(x,y)
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=2, cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');
#pyplot.contourf(X,Y,u,v,levels=20,vmin=0,vmax=2)
#pyplot.quiver(X,Y,u,v)

#pyplot.streamplot(X, Y, u, v)


pyplot.show()
       

