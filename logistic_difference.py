import numpy as np
import matplotlib.pyplot as plt
'''
Playing around with logistic difference equation.
https://www.biosym.uzh.ch/modules/models/ETHZ/Logisticdifferenceequation/lde.xhtml
'''
Niter = 1000


def logistic(r,x_i,x):
    x[0] = x_i  
    for i in range(Niter):
        x[i+1] = r*x[i]*(1-x[i])
    return(x)

x = np.zeros(Niter+1)
x_initial = 0.4    # initial "population"

r1= 3.53          # growth rate
r = np.linspace(0,4,2000)

for j in range(len(r)):
    x = logistic(r[j],x_initial,x)
    cut_off = 500
    x_uniq = np.unique(x[cut_off:-1])
    r_2 = np.ones(len(x_uniq))*r[j]
    plt.plot(r_2,x_uniq,'k.', markersize = 0.2)

plt.xlabel('iteration')
plt.ylabel('population size')
plt.show()

