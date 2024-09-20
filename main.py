import numpy as np  # type: ignore
import matplotlib as plt  # type: ignore


#SE4
#Generation subplots

fig, ax = plt.subplots()

#definition du signal
f0= 440
a0=1.0
fs=520
phi0= 2*np.pi/3

fc= f0*100  #sampling for continuous

start = -20e-3
stop = 20e-3

# sampled signal

t = np.arange(start, stop+1/fs,1/fs)
x = a0*np.sin(2*np.sin(2*np.pi*f0*t+phi0))

# "continous signal"

tc = np.arange(start,stop+1/fc,1/fc)
xc = a0*np.sin(2*np.sin(2*np.pi*f0*t+phi0))


#plot the graph 

ax.plot(t,x,'o',tc,xc,'--')

#labeling the figure

ax.set_xlabel('time',fontsize=10)
ax.set_ylabel('amplitude',fontsize=10)
ax.set_title('continuous sampled at %d Hz' %(f0,fs))

