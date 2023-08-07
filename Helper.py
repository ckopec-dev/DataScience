#
#
#
# Reusable functions
#
#
#

import sympy

def PrimesLessThanN(n):
    return len(list(sympy.sieve.primerange(0, n)))

def NoverN(n):
    return n / PrimesLessThanN(n)

