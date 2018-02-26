from math import *
import numpy as np
R=2400
L=0.78
C=6.8e-09
Q=1/R*sqrt(L/C)
w0=1/sqrt(L*C)
print('Q=',Q)
print('nu0=',w0/2/pi)
# omega_c=omega0/sqrt(2)/Q*sqrt(2*Q**2-1)
# omega_r=omega0
# omega_l=omega0/sqrt(1-1/(2*Q**2))
# omega=np.array([omega_c,omega_r,omega_l])
# print(omega/2/pi)
# c=2297/2157
# print(2213*c)