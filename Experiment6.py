#
#
#
# Primes less than n.
#
#
#

import sympy

def PiN(n):
    return len(list(sympy.sieve.primerange(0, n)))
        
print(PiN(1000))
print(PiN(1000000)) 
