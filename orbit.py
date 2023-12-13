
#!usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def euler(x,y,vx,vy):
    a = -G*M/np.sqrt((x**2 + y**2))**2
    theta = np.arctan2(y,x)
    ax = np.cos(theta)*a
    ay = np.sin(theta)*a
    x = x + t*vx
    y = y + t*vy
    vx = vx + t*ax
    vy = vy + t*ay
    return(x,y,vx,vy)

def euler_cromer(x,y,vx,vy):
    a = -G*M/np.sqrt((x**2 + y**2))**2
    theta = np.arctan2(y,x)
    ax = np.cos(theta)*a
    ay = np.sin(theta)*a

    vx = vx + t*ax
    vy = vy + t*ay
    x = x + t*vx
    y = y + t*vy
    return(x,y,vx,vy)

AU = 1.496*1e11   # 1 AU unit in meters, mean earth-sun distance
yr = 365*24*60*60 # one year in seconds
GM = 4*np.pi**2
mass = 1
G = 6.67*1e-11   # grav constant
M = 1.99*1e30    # mass of sun
m = 1.0*1e17     # mass of comet
#m = 1
t = 0.02*yr

r0 = AU
v0 = np.sqrt(G*M/r0)
#print(v0)
#print(np.sqrt(G*M/r))
#print(2*np.pi*AU/(365*24*60*60))

x = r0
y = 0
vx = 0
vy = v0

x_list = []
y_list = []
vx_list = []
vy_list = []
Ek_list = []
Ep_list = []
T_list = []
N = 1000
T = 0
for i in range(N):
    x_list.append(x)
    y_list.append(y)
    vx_list.append(vx)
    vy_list.append(vy)
    v = np.sqrt(vx**2 + vy**2)
    E_kin = 0.5*m*v**2
    Ep = -G*M*m/(np.sqrt(x**2 + y**2))
    Ek_list.append(E_kin)
    Ep_list.append(Ep)

    #x,y,vx,vy = euler(x,y,vx,vy)
    x,y,vx,vy = euler_cromer(x,y,vx,vy)
    
    T_list.append(i*t) 
    
ax = plt.subplot(111,projection = 'polar')
ax.plot(np.arctan2(y_list,x_list), np.sqrt(np.array(x_list)**2 + np.array(y_list)**2))
ax.grid(True)

plt.figure()
plt.plot(x_list,y_list)

plt.figure()
plt.plot(T_list, Ek_list, label = 'kinetic')
plt.plot(T_list, Ep_list, label = 'potential')
plt.legend()
plt.show()
