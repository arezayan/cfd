
"""
Created on Tue May  3 19:50:14 2022

@author: Amirreza
"""

import numpy
from matplotlib import pyplot,cm

# Parameters
nx = 50
ny = 50
nt  = 100
xmin = 0
xmax = 2
ymin = 0
ymax = 1

dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)

# Initialization
p  = numpy.zeros((ny, nx))
pd = numpy.zeros((ny, nx))
b  = numpy.zeros((ny, nx))
x  = numpy.linspace(xmin, xmax, nx)
y  = numpy.linspace(xmin, xmax, ny)

# Source
b[int(ny / 4), int(nx / 4)]  = 100
b[int(3 * ny / 4), int(3 * nx / 4)] = -100


for n in range(nt):
    pd=p.copy()
    for j in range(1,ny-1):
        for i in range(1,nx-1):
            p[j,i] = ((pd[j,i+1] + pd[j,i-1]) * dy**2 + (pd[j+1,i] + pd[j-1,i]) * dx**2 - b[j,i] * (dx**2) * (dy**2)) / (2 * (dx**2 + dy**2))
                      
    p[0, :] = 0
    p[-1, :] = 0
    p[:, 0] = 0
    p[:, -1] = 0



fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)
ax.view_init(30, 225)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
pyplot.show()
