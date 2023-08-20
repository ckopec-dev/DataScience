#
#
#
# The Riemann zeta function: 1 + 1 / 2^s + 1 / 3^s + ... where s is a complex number.
#
# The Riemann hypothesis claims all non-trivial zeroes of this function have real part 1/2.
#
#
#

# https://mpmath.org/doc/current/functions/zeta.html
from mpmath import *

z = zeta(-1+8j)

print(z.real)
print(z.imag)

z = zeta(complex(-1,8))

print(z.real)
print(z.imag)