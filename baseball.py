#!usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

m = 0.145
r = (7.4/2)*1e-2

Cd = 0.35 # drag coefficient
A = np.pi*r**2
rho = 1.225 # kg/m3 density of air
g = 9.81

v0 = 15               # m/s initial velocity
theta = 45*np.pi/180  # initial angle of 45

vx = np.cos(theta)*v0
vy = np.sin(theta)*v0

x0 = 0 # initial position
y0 = 0

t = 0.1      # time step
maxi = 1000  # maximum # of steps

x = x0
y = y0
X = []
Y = []
X_theo = []
Y_theo = []
x_theo = x0
y_theo = y0
vx_theo = vx
vy_theo = vy

def acc(x,y,vx,vy):
    Fa_x = -0.5*Cd*rho*A*vx**2
    Fa_y = -0.5*Cd*rho*A*vy**2
    return(1/m*Fa_x,1/m*Fa_y - g) 

def gf():
    return(0,-g)

t_1 = 0

for i in range(maxi):


    X.append(x)
    Y.append(y)
    
    X_theo.append(x_theo)
    Y_theo.append(y_theo )

    #ax,ay = acc(x,y,vx,vy) 
    ax,ay = gf() 
    vx = vx + t*ax
    vy = vy + t*ay
    x = x + t*vx
    y = y + t*vy
    

    x_theo = x0 + vx_theo*t_1 

    y_theo = y0 + vy_theo*t_1 - 0.5*g*t_1**2
    t_1 += t     

    if y_theo < 0:
        print('time: ', t_1 )
        break

print(len(Y_theo))
print(X[-1])
print(X_theo[-1])
plt.plot(X,Y, label = 'euler')
plt.plot(X_theo,Y_theo,'--x' ,label = 'analysis')
plt.legend()
plt.show()
