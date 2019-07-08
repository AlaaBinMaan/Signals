import numpy
import matplotlib.pyplot as plot

new_amplitude=[]
size_time=100
time= numpy.arange(0,100,0.01)
noise=numpy.random.normal(0,1,10000)

amplitude= numpy.cos(time)
plot.figure("figure 1",figsize=(15,5))
plot.axvline(x=size_time/2, color='black', linestyle='-')
plot.axhline(y=0, color='black', linestyle='-')
plot.title('cos wave')
plot.xlabel('Time (t)')
plot.ylabel('Amplitude (A)')
plot.grid(True, which='both')
plot.plot(time, amplitude,color="blue",label='cos wave')
plot.legend(loc='upper right')

amplitude= numpy.cos(time)+noise
plot.figure("figure 2",figsize=(15,5))
plot.axvline(x=size_time/2, color='black', linestyle='-')
plot.axhline(y=0, color='black', linestyle='-')
plot.title('cos wave')
plot.xlabel('Time (t)')
plot.ylabel('Amplitude (A)')
plot.grid(True, which='both')
plot.plot(time, amplitude,color="brown",label='cos wave with noise')
plot.legend(loc='upper right')

y=400
plot.figure("figure 3",figsize=(15,5))
plot.title('cos wave after smoothing ')
plot.xlabel('Time (t)')
plot.ylabel('Amplitude (A)')
plot.grid(True, which='both')
z=y
n=y
i=0    
size=(numpy.size(amplitude))-(y-1)
while i<size :
    total=0.0
    j=i
    while j<y:
       e1=amplitude[j]
       total=total+e1
       j=j+1
    total=total/z
    new_amplitude.append(total)
    y=y+1
    i=i+1
new_amplitude=numpy.array(new_amplitude)
z=z-1
z=float(z)
z=z*(10**-2)
size_time=size_time-z
    
time= numpy.arange(0,size_time,0.01)
plot.plot(time,new_amplitude,label='sine wave with window=%d'%n)

plot.legend(loc='upper right')