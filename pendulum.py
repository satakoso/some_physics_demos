#!usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

theta_0 = 50*(np.pi/180)  # initial angle
w0 = 0                    # initial velocity
g = 1   # use unity units
L = 1

t = 0.1  # time step

def euler(theta,w):
    a = -(g/L)*np.sin(theta)
    theta1 = theta + t*w
    w1 = w + t*a
    return(theta1,w1)

def verlet(theta1,theta2):
    a = -(g/L)*np.sin(theta)
    theta3 = 2*theta2 - theta1 + a*t**2
    return(theta3)

N = 200 # max iterations

t_list = []
theta_list = []
w_list = []
T_period = []

theta = theta_0
w = w0
t_temp = 0
for i in range(N):

    t_list.append(t_temp)
    theta_list.append(theta)

    #w_list.append(w)
    #theta,w = euler(theta,w)

    if i == 0:
        theta_minus = theta - t*w - t**2/2*(g/L)*np.sin(theta)

    theta_minus = theta_list[i-1]
    theta = verlet(theta_minus,theta)

    if (i >= 1 and theta_list[i-1]*theta_list[i] < 0):
        T_period.append(t_temp)
        
    
    t_temp += t
    

plt.plot(t_list,theta_list)
plt.xlabel('time')
plt.ylabel('angle [rad]')


plt.show()
print(T_period)
