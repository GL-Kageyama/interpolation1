#==================================================================
#----------------    Nearest-neighbor method    -------------------
#==================================================================
# Nearest-neighbor interpolation is a simple method of 
# multivariate interpolation in one or more dimensions.
#==================================================================
# Pattern 1 : Basic implementation in Python
#==================================================================
import numpy as np
import matplotlib.pyplot as plt

def get_nearest_interpolate_function(smpx, smpy):
    smpxy = zip(smpx, smpy)
    smpxy = sorted(smpxy, key=lambda t: t[0])
    smpxy = list(smpxy)
    
    def interpolate(intrx):
        if (intrx < smpxy[0][0]) | (intrx > smpxy[-1][0]):
            print("Interpolation point is not within sample point range.")
            return
        
        for idx in range(len(smpxy)):
            if intrx < smpxy[idx][0]:
                cp = (smpxy[idx - 1][0] + smpxy[idx][0]) / 2
                if intrx - cp > 0:
                    return smpxy[idx][1]
                else:
                    return smpxy[idx - 1][1]
    return interpolate

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2 / 10.0)
f = get_nearest_interpolate_function(x, y)

intrx = np.linspace(0, 10, num=101, endpoint=True)

plt.plot(x, y, 'o', intrx, [f(xi) for xi in intrx], '--')
plt.legend(['data', 'nearest'], loc='best')
plt.savefig("Nearest-neighbor_by_Basic.png", dpi=300)
plt.show()

#==================================================================
# Pattern 2 : Brent's method using Scipy's API
#==================================================================

from scipy.interpolate import interp1d

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2 / 10.0)

f = interp1d(x, y, kind='nearest')

intrx = np.linspace(0, 10, num=101, endpoint=True)

plt.plot(x, y, 'o', intrx, [f(xi) for xi in intrx], '--')
plt.legend(['data', 'nearest'], loc='best')
plt.savefig("Nearest-neighbor_by_scipy.png", dpi=300)
plt.show()

