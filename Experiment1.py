#
#
#
# Euler's identity: e^(pi*i) = -1
# 
# Complex power of e: e^z = 1 + z + z^2/1x2 + z^3/1x2x3 ... 
#
#
#

import math, cmath

z = complex(0, 1)
exp = math.pi * z
z = cmath.exp(exp)

print ("The real part of complex number is : ", z.real)
print ("The imaginary part of complex number is : ", z.imag)
print (z)

# Evaluate iteratively
print("Evaluating iteratively...")
z = complex(0, math.pi)
e = complex(1, 0)
for n in range(1, 100):
    print(n)
    e = e + (z ** n / math.factorial(n))
    print (e)

