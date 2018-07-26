
##### By Barun Basnet ######
##### Friday, July 26 ######

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import max_len_seq

PN = max_len_seq(5)[0]  #Maximum Length Sequence(MLS) code generation
PN = (PN * 2) - 1 # +1 and -1

########################################################
""" Manual Method (Without Library)
A = np.array([1,1,1,1,1]) # No of LFSR = 5
size = 31  #2^D - 1
PN = [] # Storing generated Pseudo Noise sequence
for i in range(size):
    print(A[-1])
    PN.append(A[-1])
    A = [A[-1] ^ A[-2], A[0], A[1], A[2], A[3]] # ^ XOR """
#########################################################################   
######## Injected Signal for STDR/SSTDR ################      
       
x = np.arange(0, 1+0.01, 0.01) 
Carrier = np.sin(2 * np.pi * x)

Inject = []
for i in range(len(PN)):
  Inject = Inject + [PN[i]*Cr for Cr in Carrier]


plt.plot(PN)
plt.plot(Carrier)
plt.plot(Inject)
####################################
####### Reflected Signal ###########

Noise = (np.random.normal(0, 1, len(Inject))) #*0.5 # Approximation on white noise
plt.plot(Noise)

Reflect = (Inject + Noise) #* 0.8          #Attenuation of the signal
plt.plot(Reflect)
#######################################
###### Auto-correlation################

result = np.correlate(Inject, Reflect, mode="same")
plt.plot(result)

#######################################
######Normalized Auto-correlation (-1 to +1) ######

xx, yy = 0, 0

for i in range(len(Inject)):
    xx = xx + Inject[i]**2
    yy = yy + Reflect[i]**2
    
zz = math.sqrt(xx*yy)
plt.plot(result/zz)
#############################################







