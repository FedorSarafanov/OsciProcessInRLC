import numpy as np
from numpy import pi,sqrt, linspace
import matplotlib.pyplot as plt

with open('r100.tsv', 'r') as datafile:
	strings=datafile.read().split()
	del strings[0:4]
	numbers = list(map(float, strings))
	nu=np.array(numbers[0::4])
	w=nu*2*pi
	uc=np.array(numbers[1::4])
	ur=np.array(numbers[2::4])
	ul=np.array(numbers[3::4])
	e0=np.min(uc)
	Q=np.max(uc)/np.min(uc)
	nu0=nu[np.argmax(ur)]
	w0=nu0*2*pi

print('Q=',Q)
print('nu0=',nu0)
print('w0=',w0)

C=6.8e-09
R=1/C/w0/Q
L=1/C/w0**2
L= 0.6861506965061832
print('e0=',e0,'<=из эксперимента')
print('C=',C,'<=считаем известным')
print('R=',R,'<=казалось 2400')
print('L=',L,'<=казалось 0.78')
w_th=linspace(1,20000,500)
uc_th=e0*w0**2/sqrt(w0**2*w_th**2/Q**2+(w_th**2-w0**2)**2)
uc_th=e0*w0**2/sqrt(w0**2*w_th**2/Q**2+(w_th**2-w0**2)**2)
ul_th=e0*w_th**2/sqrt(w0**2*w_th**2/Q**2+(w_th**2-w0**2)**2)
ur_th=e0*w0*w_th/sqrt(w0**2*w_th**2+Q**2*(w_th**2-w0**2)**2)
plt.plot(w,uc,'r.')
plt.plot(w,ul,'g.')
plt.plot(w,ur,'b.')
plt.plot(w_th,uc_th,'r')
plt.plot(w_th,ul_th,'g')
plt.plot(w_th,ur_th,'b')
plt.xlim( (1.25e4, 1.64e4) ) 
# plt.plot(nu,ur)
# plt.plot(nu,ul)
plt.show()