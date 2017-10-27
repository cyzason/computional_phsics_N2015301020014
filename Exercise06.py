import matplotlib.pyplot as plt
import numpy as np
import math
dt=1
t=[0]*100
F0=0.2
w0=[3]*100
z0=[0]*100
F1=0.4
w1=[3]*100
z1=[0]*100
F2=0.8
w2=[3]*100
z2=[0]*100
for i in range (0,99):    
    t[i+1] = t[i] + 1
    z0[i+1] = z0[i]+w0[i]* dt
    w0[i+1]=w0[i]-10*np.sin(z0[i])*dt-0.5*w0[i]*dt+F0*np.sin(0.5*t[i])*dt
    z1[i+1] = z1[i]+w1[i]* dt
    w1[i+1]=w1[i]-10*np.sin(z1[i])*dt-0.5*w1[i]*dt+F1*np.sin(0.5*t[i])*dt
    z2[i+1] = z2[i]+w2[i]* dt
    w2[i+1]=w2[i]-10*np.sin(z2[i])*dt-0.5*w2[i]*dt+F2*np.sin(0.5*t[i])*dt
plt.plot(t, z0,'r--.')      
plt.plot(t, z1,'b--.')
plt.plot(t, z2,'g--.')      
plt.xlabel("t") 
plt.ylabel("y")
plt.title('z-t relation') 
plt.legend(labels = ['F=0.2', 'F=0.4','F=0.8',])
plt.show()