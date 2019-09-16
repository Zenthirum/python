from matplotlib.pyplot import *
import numpy as np
#figsize (5,5)
#imshow(np.random.rand(10,10), interpolation="nearest")
#show()
#input("")
#imshow(np.random.rand(10,10), interpolation="lanczos")
#plot([1,2,3,4])
#show()

def mandel(c, maxiter):
    z = complex(0,0)

    for iteration in range(maxiter):
        z = (z*z) + c
        pass
    
    return iteration

def iter_z2_plus_c(c, maxiter):
    values = [complex(0,0) for i in range(maxiter)]
    z = complex(0,0)

    values[0] = z

    for i in range(1, maxiter):
        z = (z*z)+c
        values[i] = z

    return values

v = iter_z2_plus_c(complex(0.4+0.41), 10)
print(v)
