import numpy as np
import scipy.constants as sc

v0 = 0.99
gamma = 1 / np.sqrt(1 - v0**2)
L0 = 200
tb = L0 / v0
c = sc.c

print(-v0*gamma*L0 + gamma*tb)
print(L0 / (gamma**2*v0))
print(L0 / v0 + L0*v0)
print(L0/v0 + L0*v0)
print(L0/v0 - L0*v0)

g = -0.1 / c * (365*60*60*24)          # Fra s til år og fra SI til nat

tp = tb - v0/g
print(tp)

# La ty = tp

def v(t):
    return v0 + g*(t - tb)

# Funksjon som regner tiden sett på Homey fra rakettframen som funksjon a tid sett på Homey fra Homeyframen
def tym(t):
    if isinstance(t, (float, int)):
        if t > tb:
            return t*gamma
        else:
            return t - v(t)*(L0 + v0*(t - tb) + 0.5*g*(t - tb)**2)
    else:
        normal = np.where(t < tb)
        accelerated = np.where(t >= tb)

        tym_n = t[normal]/gamma**2
        tym_a = t[accelerated] - v(t[accelerated])*(L0 + v0*(t[accelerated] - tb) + 0.5*g*(t[accelerated] - tb)**2)
        tym_array = np.concatenate((tym_n, tym_a))
        return tym_array

print(tym(tp))

# Merk : ty = tym(tp)

import matplotlib.pyplot as plt

ty = np.linspace(0, tp, 200)
plt.plot(ty, tym(ty), label=r'$t_{Y\prime}\;[yr]$')
plt.xlabel(r'$t_Y\;[yr]$', weight='bold', fontsize=16)
plt.ylabel(r'$t_{Y\prime}\;[yr]$', weight='bold', fontsize=16)
plt.legend(prop={'size': 16})
plt.savefig('time_plot.png')
plt.show()

print(tp - 4 + tp - 4 + 4)          # 292 + 292 + 4

Tm = (v0*np.sqrt(1 - v0**2) + np.arcsin(v0)) / (-2*g)
print(Tm)
