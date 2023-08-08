#
#
#
# The Prime Number Theorem: n(N) ~ N / log N
#
#
#

import math
from Helper import *
from tabulate import tabulate

N = [100, 1000, 1000, 10000, 100000, 1000000]
calcs = []

for n in N:
    logN = math.log(n)
    nOverPiN = NoverPiN(n)
    error = ((logN - nOverPiN) / nOverPiN) * 100
    calcs.append([n, logN, nOverPiN, error])
    
print(tabulate(calcs, headers=['N', 'log(N)', 'N/Pi(N)', '% error']))
