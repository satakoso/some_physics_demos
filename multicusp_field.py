import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy
from scipy.spatial.transform import Rotation as R

# dimensions of the magnets
dimensions = (0.75,0.75,0.75)
c1 = magpy.magnet.Cuboid(magnetization = (-100,0,0), dimension = dimensions, position = (2,0,0) )
c2 = magpy.magnet.Cuboid(magnetization = (0,-100,0), dimension = dimensions, position = (0,2,0) )
c3 = magpy.magnet.Cuboid(magnetization = (100,0,0), dimension = dimensions, position = (-2,0,0) )
c4 = magpy.magnet.Cuboid(magnetization = (0,100,0), dimension = dimensions, position = (0,-2,0) )

# orientation of the magnets
b = 100*np.cos(np.pi/4)
a = 2.0*np.cos(np.pi/4)
#r = R.from_euler('z', -45, degrees=True)
c5 = magpy.magnet.Cuboid(magnetization = (0,100,0), dimension = dimensions, position = (a,a,0) )
c5.orientation = R.from_euler('z', -45, degrees=True)
c6 = magpy.magnet.Cuboid(magnetization = (-100,0,0), dimension = dimensions, position = (-a,a,0) )
c6.orientation = R.from_euler('z', -45, degrees=True)
c7 = magpy.magnet.Cuboid(magnetization = (0,-100,0), dimension = dimensions, position = (-a,-a,0) )
c7.orientation = R.from_euler('z', -45, degrees=True)
c8 = magpy.magnet.Cuboid(magnetization = (100,0,0), dimension = dimensions, position = (a,-a,0) )
c8.orientation = R.from_euler('z', -45, degrees=True)

c = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
c.show()

ts = np.linspace(-2.5,2.5,50)
grid = np.array([[(x,y,0) for x in ts] for y in ts])

B = magpy.getB(c,grid)
Bamp = np.linalg.norm(B,axis = 2)
Bamp /= np.amax(Bamp)

print(B[:,:,0])
print('---')
print(B[:,:,2])
fig,ax = plt.subplots()

# plot the superposition of the magnetic field
ax.streamplot(
    grid[:,:,0], grid[:,:,1], B[:,:,0], B[:,:,1],
    density=1.5,
    color='black'
)
plt.savefig('multicusp_field1.svg')
plt.savefig('multicusp_field.png')
plt.savefig('multicusp_field.pdf')
plt.show()
#ax1.streamplot(
#    grid[:,:,0],
