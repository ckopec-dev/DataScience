#
#
#
# Euler's identity: e^(pi*i) = -1
#
#
#

import math, cmath

z = complex(0, 1)
exp = math.pi * z
z = cmath.exp(exp)

print ("The real part of complex number is : ", z.real)
print ("The imaginary part of complex number is : ", z.imag)

# Evaluate iteratively

for n in range(1, 4):
    print("TODO")    
