import matplotlib.pyplot as plt
import numpy as np
from math import *

def triangle_signal(t,periode):
    return 2/periode*(t-periode*floor(t/periode + 1/2))*(-1)**floor(t/periode + 1/2)


sample_size = 20
x = [i/10 for i in range (int(-sample_size/2),int(sample_size/2))]
y = [triangle_signal(x[i],1) for i in range (sample_size)]

print(x)
print(y)


# x axis values
a = [1,2,3]
# corresponding y axis values
b = [2,4,1]
plt.plot(a,b)
plt.show()