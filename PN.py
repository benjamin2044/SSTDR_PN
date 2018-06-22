##### By Barun Basnet ######
##### Friday, June 22 ######

import numpy as np
import matplotlib.pyplot as plt
import math

A = np.array([1,1,1,1,1,1]) # No of LFSR = 6

size = 63  #2^D - 1

PN = [] # Storing generated Pseudo Noise sequence


for i in range(size):
    print(A[-1])
    PN.append(A[-1])
    A = [A[-1] ^ A[-2], A[0], A[1], A[2], A[3], A[4]] # ^ XOR
    
########################################################## 
## Matching with voltage levels, i.e 1 = -1, 0 = 1       
for i in range(size):
    if PN[i]==1:
        PN[i]=-1;
    else:
        PN[i]=1
################################### 
### Injected Signal #######
### SSTDR/STDR ################
        
x = np.arange(0, 63) 
carrier = np.sin(x)   
inject = PN * carrier
plt.plot(x, PN)
plt.plot(x, carrier)
plt.plot(x, inject)
####################################
####### Reflected Signal ###########

noise = (np.random.normal(0, 1, 63)) * 0.5  # Approximation on white noise
reflect = (inject + noise) * 0.8            #Attenuation of the signal
plt.plot(x, reflect)
#######################################
###### Auto-correlation################

result = np.correlate(inject, reflect, mode="same")
plt.plot(x, result)

#######################################
######Normalized Auto-correlation######

xx, yy = 0, 0

for i in range(63):
    xx = xx + inject[i]**2
    yy = yy + reflect[i]**2
    
zz = math.sqrt(xx*yy)
plt.plot(x, result/zz)
