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
    nOverN = NoverN(n)
    error = ((logN - nOverN) / nOverN) * 100
    calcs.append([n, logN, nOverN, error])
    
print(tabulate(calcs, headers=['N', 'log N', 'N over n(N)', '% error']))
