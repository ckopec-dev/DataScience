#
#
#
# The Riemann zeta function: 1 + 1 / 2^s + 1 / 3^s + ... where s is a complex number.
#
# The Riemann hypothesis claims all non-trivial zeroes of this function have real part 1/2.
#
#
#

from Helper import *
import math, cmath

print(Zeta(complex(1.1, 0), 1000000))
print(Zeta(complex(1.5, 0), 1000000))
