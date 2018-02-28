import numpy as np
from numpy import pi,sqrt, linspace
import matplotlib.pyplot as plt
from random import uniform as uniform

def processing(name,saveto, om):
	plt.cla()
	# with open('r2400_0.2541.tsv', 'r') as datafile:
	# with open('r100.tsv', 'r') as datafile:
	with open(name, 'r') as datafile:
		strings=datafile.read().split()
		del strings[0:4]
		numbers = list(map(float, strings))
		nu=np.array(numbers[0::4])
		uc=np.array(numbers[1::4])
		ur=np.array(numbers[2::4])
		ul=np.array(numbers[3::4])

	w=nu*2*pi
	e0=np.min(uc)#*0.992
	Q=np.max(uc)/e0
	nu0=nu[np.argmax(ur)]
	nu0c=nu[np.argmax(uc)]
	nu0l=nu[np.argmax(ul)]
	w0=nu0*2*pi
	C=6.8e-09
	R=1/C/w0/Q
	L=1/C/w0**2

	Rp=float(om)
	Lp=0.708
	Cp=6.8e-09

	print('Q сравнением (по нему график)=',Q)
	if Rp==2400:
		print('Q методом ширины (2400)=',w0/abs(12379-16181))
		print('DeltaOmega=',abs(12379-16181))
	else:
		print('Q методом ширины (100)=',w0/abs(14211-14919))
		print('DeltaOmega=',abs(14211-14919))

	print('Q расчетом=',1/Rp*sqrt(Lp/Cp))

	print('nu0=',nu0)
	print('nu0с=',nu0c)
	print('nu0l=',nu0l)
	print('w0=',w0)
	print('e0=',e0,'<=из эксперимента')
	print('C=',C,'<=считаем известным')
	print('R=',R,'<=предполагалось',om)
	print('L=',L,'<=предполагалось 0.78')

	w_th=linspace(1,20000,500)

	# Q=np.max(uc)/e0*0.992
	Q=np.max(uc)/e0

	# def uct(w):
		# return e0*w0**2/sqrt(w0**2*w**2/Q**2+(w**2-w0**2)**2)

	uc_th=e0*w0**2/sqrt(w0**2*w_th**2/Q**2+(w_th**2-w0**2)**2)
	ul_th=e0*w_th**2/sqrt(w0**2*w_th**2/Q**2+(w_th**2-w0**2)**2)
	ur_th=e0*w0*w_th/sqrt(w0**2*w_th**2+Q**2*(w_th**2-w0**2)**2)*0.91

	# for i in range(0,len(w)):
		# d=0.001
		# uniform(a,b)
	u_eff=np.max(uc)/sqrt(2)
	plt.axhline(y=u_eff, color='r', linestyle='-',linewidth=0.5)
	#здесь получена \Delta\omega:
	# print('\Delta\omega=',abs(12379-16181))
	plt.plot(w,uc,'r.')
	plt.plot(w,ul,'g.')
	plt.plot(w,ur,'b.')
	# plt.plot(w,ur*2.5,'m.')

	plt.plot(w_th,uc_th,'r',label=u'$U_C$')
	plt.plot(w_th,ul_th,'g',label=u'$U_L$')
	plt.plot(w_th,ur_th,'b',label=u'$U_R$')


	# plt.xlim( (1.25e4, 1.64e4) )
	plt.rc('text', usetex=True)
	plt.rc('text.latex', unicode=True)
	plt.rc('text.latex', preamble=r'\usepackage[utf8]{inputenc}')
	plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
	plt.rc('font', family='serif')
	plt.xlabel(u'$\omega$, рад/с')
	plt.ylabel(u'$u$, вольт')
	plt.title(u"Резонансные кривые, R="+om+"ом", color='gray')
	plt.legend()

	# plt.savefig(saveto, format='pdf')
	plt.show()

processing('r2400_0.2541.tsv','../plot/r2400.pdf','2400')
print('----------------')
processing('r100.tsv','../plot/r100.pdf','100')