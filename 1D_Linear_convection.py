
#1D convection equation by FDM
import numpy as np
from matplotlib import pyplot
#pre-processing
l=2 #in meter
nx=41
dx=l/(nx-1)

nt=25
sigma=0.5
dt=dx*sigma

#solving
u=np.zeros(nx)
u[:]=1
u[int(0.5/dx):int((1/dx) + 1)]=2

u0=u.copy()
un=np.zeros(nx)
for n in range(nt):
    un=u.copy()
    for i in range(1,nx):
        u[i]=un[i] - (un[i]*dt/dx*(un[i]- un[i-1]))
        u[0]=u[-1]=1


#post-processing
x=np.linspace(0,l,nx)
pyplot.plot(x,u)
pyplot.plot(x,u0)
pyplot.show()
print(u)


