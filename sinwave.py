import numpy as np
import matplotlib.pyplot as plt

ts=input("Enter TIME period:")
fs=input("Enter sampling frequency")
amp=input("Enter amplitude:")

def swave(ti):	#ti is samples passed
	return amp * np.sin(2 * np.pi *f * ti)

f=1.0/ts
at=np.linspace(0,ts,10e5)	#time constranints for plotting graph
qbits   =input("Enter quantization bits:")
qlevels =pow(2,qbits)
qstep   =1.0/qlevels
sp=1.0/fs
s_num= ts /sp
st=np.linspace(0,ts,s_num)
sample_sig=swave(st)
quant_sig=np.round(sample_sig/qstep)*qstep #rounding of sample signal

if fs<2*f:
	print "Sampling frequency is less than twice of carrier frequency."
else: 
	i=input("1. Continuous wave 2. Discrete samples 3.combined waves 4.Exit  Enter your Choice")
while i!=4:
	if i==1: 
		plt.plot (at,swave(at))
		plt.title("Sine wave")
		plt.xlabel("Time")
		plt.ylabel("Amplitude")
		plt.show()
	elif i==2:
		plt.stem (st,sample_sig)
		plt.title("Sample points")
		plt.xlabel("Time")
		plt.ylabel("Amplitude")
		plt.show()
	elif i==3:
		plt.plot (at,swave(at))
		plt.stem (st,sample_sig)
		plt.title("Combined Sample points and Sine wave")
		plt.xlabel("Time")
		plt.ylabel("Amplitude")
		plt.show()
	i=input("1. Continuous wave 2. Discrete samples 3.combined waves 4.Exit  Enter your Choice")

#OUTPUT:
# [fedora@localhost ~]$ python sinwave.py
# Enter TIME PERIOD :3
# Enter Sampling Frequency :3
# Enter Amplitude :2
# enter quantization bits:2
#1. Continuous wave 2. Discrete samples 3.combined waves 4.Exit  Enter your Choice1
#1. Continuous wave 2. Discrete samples 3.combined waves 4.Exit  Enter your Choice2
#1. Continuous wave 2. Discrete samples 3.combined waves 4.Exit  Enter your Choice3
#1. Continuous wave 2. Discrete samples 3.combined waves 4.Exit  Enter your Choice4
# [fedora@localhost ~]$
