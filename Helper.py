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

def Basel(exp, terms):
    val = 0
    for n in range (1, terms + 1):
        val = val + (1 / n ** exp)
    return val