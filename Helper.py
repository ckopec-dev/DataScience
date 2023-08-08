#
#
#
# Reusable functions
#
#
#

import sympy

def PiN(n):
    # The number of primes less than n.
    return len(list(sympy.sieve.primerange(0, n)))

def NoverPiN(n):
    return n / PiN(n)

def Basel(exp, terms):
    # 1 + 1 / 2^n + 1 / 3^n + 1 / 4^n + ...
    val = 0
    for n in range (1, terms + 1):
        val = val + (1 / n ** exp)
    return val

def Zeta(s, terms):
    # 1 + 1 / 2^s + 1 / 3^s + ... where s is a complex number.
    val = complex(0, 0)
    for n in range(1, terms + 1):
        val = val + (1 / n ** s)
    return val

