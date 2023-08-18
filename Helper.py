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

def Zeta(r,i,E=1e-24):
    # 1 + 1 / 2^s + 1 / 3^s + ... where s is a complex number.
    #https://codegolf.stackexchange.com/questions/75277/evaluate-the-riemann-zeta-function-at-a-complex-number
    R=0;I=0;n=0;
    while(True):
        a=0;b=0;m=2**(-n-1)
        for k in range(0,n+1):
            M=(-1)**k*np.prod([x/(x-(n-k))for x in range(n-k+1,n+1)]);A=(k+1)**-r;t=-i*np.log(k+1);a+=M*A*np.cos(t);b+=M*A*np.sin(t)
        a*=m;b*=m;R+=a;I+=b;n+=1
        if a*a+b*b<E:break
    A=2**(1-r);t=-i*np.log(2);a=1-A*np.cos(t);b=-A*np.sin(t);d=a*a+b*b;a=a/d;b=-b/d
    val = complex(R*a-I*b,R*b+I*a)
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