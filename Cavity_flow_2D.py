import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

nx = 41
ny = 41
nt = 500
nit = 50
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)

rho = 1
nu = .1
dt = .001

u = numpy.zeros((ny, nx))
v = numpy.zeros((ny, nx))
p = numpy.zeros((ny, nx)) 
b = numpy.zeros((ny, nx))

for j in range(1,ny-1):
    for i in range(1,nx-1):
        b[j,i]=(rho * ((u[j,i+1] - u[j,i-1]) / (2*dx*dt ) + ((v[j+1,i] - v[j-1,i]) / (2*dy*dt)))) - (u[j,i+1] - u[j,i-1]) / (2*dx*dt ) * (u[j,i+1] - u[j,i-1]) / (2*dx*dt ) - 2 * ((u[j+1,i] - u[j-1,i]) / 2*dy) * ((v[j,i+1] - v[j,i-1]) / 2*dx) - ((v[j+1,i] - v[j-1,i]) / 2*dy) * ((v[j+1,i] - v[j-1,i]) / 2*dy)
print(b)