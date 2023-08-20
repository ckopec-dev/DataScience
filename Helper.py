#
#
#
# Reusable functions
#
#
#

import sympy
import math, cmath
import numpy as np

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
    
def LogIntegral(x, terms):
    # https://math.stackexchange.com/questions/700391/integration-by-parts-of-the-logarithmic-integral
    # li(x) = Ei(lnx) = (γ + ln(lnx)) + [the cumulative sum from n=1 to infinity of: ((lnx)^n)/(n*n!)]
    if x <= 0:
        return math.nan 
    y = 0.5772156649015328606065120
    l1 = math.log(x)
    if l1 <= 0:
        return math.nan
    val = y + math.log(l1)
    for n in range(1, terms + 1):
        val = val + (l1**n)/(n * math.factorial(n))
    #if x > 2: val = val - 1.04516378011749278
    return val

def ComplexMatrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def IsPure(c):
    # True if either the real or imaginary part is 0.
    return (math.isclose(c.real, 0, abs_tol = 0.001)) or (math.isclose(c.imag, 0, abs_tol = 0.001))